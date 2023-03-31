import requests
from datetime import datetime
import smtplib
import os


MY_LAT = os.environ.get("Your_latitude")
MY_LONG = os.environ.get("Your_longitude")
USER_NAME= os.environ.get("GMAIL")
PASSWORD= os.environ.get("PASSWORD")



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


