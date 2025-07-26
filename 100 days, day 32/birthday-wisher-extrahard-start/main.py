##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
my_email = "cc.in"
pwd = "eut"



import smtplib
import datetime as dt
import random
import pandas as pd

letter_addresses = [r"C:\Useemplates\letter_3.txt"]

birthdays = pd.read_csv(r"C:\Udays.csv")

now = dt.datetime.now()
today = now.day
this_month = now.month

for index,row in birthdays.iterrows():
    if (row["month"] == this_month) and (row.day==today):
        recepient = row["email"]
        recepient_name = row["name"]
        
        message_address = random.choice(letter_addresses)
        with open(message_address) as message_list:
            message = message_list.readlines()
        final_message = ""
        for i in range(len(message)):
            if i == 0:
                message[0] = message[0].replace("[NAME]",recepient_name)
            final_message += message[i]
        ## print(final_message)
        """message[0] = message[0].replace("[NAME]", recepient_name)
        message[0] = list(message[0])
        message[0] = "".join(message[0])
        print(message[0]+(message[1:]))"""

        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=my_email,password=pwd)
        connection.sendmail(
            to_addrs=recepient,
            from_addr=my_email,
            msg=f"Subject:Happy Birthday {recepient_name}\n\n{final_message}")