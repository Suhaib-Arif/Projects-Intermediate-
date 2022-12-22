import smtplib
import requests
import os

EMAIL=os.environ["EMAIL"]
PASSWORD=os.environ["PASSWORD"]

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
news_api_key = os.environ["NEWS_API_KEY"]
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

Stock_api = os.environ["STOCK_API_KEY"]

parmeters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": Stock_api
}

response = requests.get(url=STOCK_ENDPOINT, params=parmeters)
data = response.json()["Time Series (Daily)"]


new_data=[value for (key,value) in data.items() ]

yesterday_stock=float(new_data[0]["4. close"])
previous_day_stock=float(new_data[1]["4. close"])


positive_difference = abs(yesterday_stock - previous_day_stock)
average = (yesterday_stock + previous_day_stock) / 2
percentage_difference = (positive_difference / average) * 100

if percentage_difference > 5:
    news_parameter = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key
    }

    news_data = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news = news_data.json()["articles"]

    news = news[:3]
    news_articles=[f"Headline:{item['title']} \n\n Description:{item['description']}" for item in news]

    print(news_articles)

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)

        for article in news_articles:
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Todays Stock\n\n{article}"
            )


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""



##########################################################TRASH#############################################################

# time = dt.datetime.now()
#
# today = time.today().date()
#
# is_weekday = True
# days_count = 1
#
# while is_weekday:
#     yesterday = today - dt.timedelta(days=days_count)
#
#     if yesterday.weekday() in [5, 6]:
#         days_count += 1
#     elif yesterday.weekday() == 0:
#         previous_day = yesterday - dt.timedelta(days=3)
#         is_weekday = False
#     else:
#         previous_day = yesterday - dt.timedelta(days=1)
#         is_weekday = False
#
# yesterday_key = yesterday.strftime("%Y-%m-%d")
# previous_day_key = previous_day.strftime("%Y-%m-%d")
#
#
# yesterdays_stock = float(data["Time Series (Daily)"][yesterday_key]['4. close'])
# previous_day_stock = float(data["Time Series (Daily)"]["2022-11-07"]['4. close'])
#
# print(yesterdays_stock)
# print(previous_day_stock)
#
