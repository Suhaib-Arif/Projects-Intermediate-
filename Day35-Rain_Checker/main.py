import requests
import os

api_key=os.eviron.get("API_KEY")



from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTHURIZATION")


parameters={
    "lat":os.environ.get("LATTITUDE"),
    "lon":os.environ.get("LONGITUDE"),
    "exclude":"current,minutely,daily",
    "appid":api_key
}

result=requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
result.raise_for_status()
weather_data=result.json()

weather_data_slice=weather_data["hourly"][:12]

will_rain=False

for hour in weather_data_slice:
    if hour["weather"][0]["id"] < 700:
        will_rain=True
print(will_rain)

if will_rain:
    client=Client(account_sid,auth_token)

    message=client.messages.create(
        body="Rain rain go away, come again another day",
        from_=os.environ.get("BOT_NUMBER"),
        to=os.environ.get("USER_NUMBER")
    )

    print(message.status)


