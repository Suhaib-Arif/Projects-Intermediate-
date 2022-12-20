from random import choice
import datetime as dt
import smtplib

email="me@gmail.com"
password="password"


with open("quotes.txt") as quotes_file:
    quotes=quotes_file.readlines()

random_quote=choice(quotes)

time=dt.datetime.now()

if time.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="you@gmail.com",
            msg=f"Subject:MOTIVATION\n\n{random_quote}"
        )

print("heyyy")
