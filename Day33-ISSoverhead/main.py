import requests
from datetime import datetime
import smtplib



MY_LAT = -44.0152 # Your latitude
MY_LONG = 166.5922 # Your longitude
USER_NAME="suhaibarifsiddiqui@gmail.com"
PASSWORD="pugbixmewevqvtlk"



def close_to_cur_pos(lat,long):
    global MY_LAT
    global MY_LONG

    if MY_LAT-5 < lat < MY_LAT+5 and MY_LONG - 5 < long < MY_LONG + 5:
        return True
    return False


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# print(iss_latitude)
# print(iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


#If the ISS is close to my current position
if close_to_cur_pos(iss_latitude,iss_longitude) and time_now.hour > sunset:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=USER_NAME,password=PASSWORD)
        connection.sendmail(from_addr=USER_NAME,to_addrs=USER_NAME,msg="SUBJECT:LOOK UP")
        print("mail sent")


# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



