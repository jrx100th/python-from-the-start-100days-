# import smtplib

# my_email = "cn"
# password = "e" # app password

# # creating a connection through the server
# with (smtplib.SMTP("smtp.gmail.com",587)) as connection:

#     # TLS stand for transport layer security  # way of securing our connection to our email server # encrypting our mail
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="jem", 
#         msg="Subject:HBD\n\nHello there!!\nThis is body of my email."
#         )




# import datetime as dt

# now = (dt.datetime.now()) # will get the current dat and time

# # creating a date time object

# dob = dt.datetime(year=1987, month=4,day=12, hour=4, minute=30, second=12)
# print(dob)


# Monday Motivational Quote 

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day = now.weekday()

# print(day)

with open(r"C:txt", mode="r") as quotes:
    quotes_list = quotes.readlines()

todays_quote = random.choice(quotes_list)

my_email = "chn"
pwd = "et"

if day == 4:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Testing Motivation\n\n{todays_quote}"
            )