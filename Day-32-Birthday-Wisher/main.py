##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

import pandas
birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

import datetime as dt

now = dt.datetime.now()
today_month = now.month
today_day = now.day

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
import random

name_text = "[NAME]"

for entry in birthday_dict:
    if entry["month"] == today_month and entry["day"] == today_day:
        letter_num = random.randint(1, 3)
        name = entry["name"]
        email = entry["email"]
        with open(f"letter_templates/letter_{letter_num}.txt", mode="r") as letter_file:
            draft_letter = letter_file.read()
            birthday_letter = draft_letter.replace(name_text, name)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib

my_email = "arielchancodes@gmail.com"
password = "bofgyvlirfloytff"
with smtplib.SMTP("smtp.gmail.com") as connection:
    #Make connection secure and encrypts email
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=f"{email}",
        msg=f"Subject:Happy Birthday\n\n{birthday_letter}"
    )

