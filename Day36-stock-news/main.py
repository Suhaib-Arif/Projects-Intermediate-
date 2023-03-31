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
