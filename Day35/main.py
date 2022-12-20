import requests

api_key="b239ad6816f4e09d41069588e7ac2d80"



from twilio.rest import Client

account_sid = 'ACd3ef97a47b820151765171253e3e09cf'
auth_token = '71c1c7a8bf0e0cbf8056f3fdf82706c8'


parameters={
    "lat":3.763386,
    "lon":103.220184,
    "exclude":"current,minutely,daily",
    "appid":api_key
}

result=requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
result.raise_for_status()
weather_data=result.json()

weather_data_slice=weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain=False

for hour in weather_data_slice:
    # print(hour["weather"][0]["id"])
    if hour["weather"][0]["id"] < 700:
        will_rain=True
print(will_rain)

if will_rain:
    client=Client(account_sid,auth_token)

    message=client.messages.create(
        body="Rain rain go away, come again another day",
        from_='whatsapp:+14155238886',
        to='whatsapp:+919731903548'
    )

    print(message.status)


