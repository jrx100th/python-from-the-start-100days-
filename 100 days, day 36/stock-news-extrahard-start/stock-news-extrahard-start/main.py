import requests
from datetime import datetime, timedelta
import pytz
import smtplib
from email.mime.text import MIMEText

STOCK_COMPANY = "Tesla"
STOCK_SYMBOL = "TSLA"
av_s = "https://www.alphavantage.co/query"

parameters1 = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK_SYMBOL,
    "apikey" : "C**************8"
}


data = (requests.get(url=av_s, params=parameters1)).json()

print(data)
# print(data.json())
# the api is fucked up


dates = list(data["Time Series (Daily)"])
today_data = data["Time Series (Daily)"][dates[0]]
yesterdayData = data["Time Series (Daily)"][dates[1]]

today_open = float(today_data['1. open'])
yesterday_close = float(yesterdayData['4. close'])
change = round((today_open-yesterday_close),3)

percentage_change = (abs(change)*100/yesterday_close)

news_site = "https://newsapi.org/v2/everything?"

# tap into date time module and get the relevant dates

ny_tz = pytz.timezone('America/New_York')
today_date = datetime.now(ny_tz).date()
yesterday_date = today_date-timedelta(days=1)

# print(today_date)
# print(yesterday_date)

np = {
    "qInTitle" : STOCK_COMPANY,
    "language" : "en",
    # "domains": "reuters.com,techcrunch.com,cnbc.com,bloomberg.com",
    "from" : yesterday_date,
    "apiKey" : "2******************************9",
    "sortBy" : "popularity"
}

news_data = (requests.get(url=news_site, params=np)).json()



source1 = (news_data["articles"][0]["source"]["name"])
source2 = (news_data["articles"][1]["source"]["name"])
source3 = (news_data["articles"][2]["source"]["name"])

author1 = (news_data["articles"][0]["author"])
author2 = (news_data["articles"][1]["author"])
author3 = (news_data["articles"][2]["author"])

title1 = (news_data["articles"][0]["title"])
title2 = (news_data["articles"][1]["title"])
title3 = (news_data["articles"][2]["title"])

description1 = (news_data["articles"][0]["description"])
description2 = (news_data["articles"][1]["description"])
description3 = (news_data["articles"][2]["description"])

content1 = (news_data["articles"][0]["content"])
content2 = (news_data["articles"][1]["content"])
content3 = (news_data["articles"][2]["content"])

url1 = (news_data["articles"][0]["url"])
url2 = (news_data["articles"][1]["url"])
url3 = (news_data["articles"][2]["url"])


mail = "c*******************************n"
pwd = "j**************p"
recepient = "c********************************"


Message1 = f"Tesla share value changed by {percentage_change}USD as of today morning\nPossible Reasons :\n1.                   {author1} from {source1}\nTitle : {title1}\n\nAvailable Info : \n{content1}\n\n{description1}\n\nMore at : {url1}"
Message2 = f"2.                   {author2} from {source2}\nTitle : {title2}\n\nAvailable Info : \n{content2}\n\n{description2}\n\nMore at : {url2}"
Message3 = f"3.                   {author3} from {source3}\nTitle : {title3}\n\nAvailable Info : \n{content3}\n\n{description3}\n\nMore at : {url3}"

report = f"{Message1}\n\n{Message2}\n\n{Message3}"
msg = MIMEText(report, 'plain', 'utf-8')
msg['Subject'] = "TSLA Share notice"
msg['From'] = mail
msg['To'] = recepient
print(msg)
if percentage_change > 4:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=mail, password=pwd)
        connection.sendmail(
            from_addr=mail, 
            to_addrs=recepient, 
            msg=msg.as_string()
        )


