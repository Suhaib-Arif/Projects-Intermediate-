##################### Extra Hard Starting Project ######################
import pandas
import datetime as df
from random import choice
import smtplib

user="suhaibarifsiddiqui@gmail.com"
password="mvtahypvktyufbez"

file=choice(["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"])


# 1. Update the birthdays.csv
birthday_data=pandas.read_csv("birthdays.csv")

birthdays=(birthday_data['day'].astype(str)) +"-"+(birthday_data.month.astype(str))
birthday_list=birthdays.to_list()

# print(birthday_list)

date=df.datetime.now()
todays_date=date
todays_date=todays_date.strftime("%d-%m")

# print(todays_date)

# 2. Check if today matches a birthday in the birthdays.csv

if todays_date in birthday_list:
    birthday_name=(birthday_data[birthdays == todays_date].name).to_string(index=False)
    email=(birthday_data[birthdays == todays_date].email).to_string(index=False)


    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(file) as file:
        letter=file.read()
        letter=letter.replace("[NAME]",birthday_name)

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=user,password=password)
        connection.sendmail(
            to_addrs=user,
            from_addr=email,
            msg=f"Subject:HAPPY BIRTHDAY!!!!!\n\n{letter}"
        )



# 4. Send the letter generated in step 3 to that person's email address.
