import requests
import os
import datetime as dt
from twilio.rest import Client

account_sid = "AC4ddd0868bf10e1c086383096c8a12cf6"
auth_token = os.environ.get("AUTH_TOKEN")
twilio_phone_number = os.environ.get("TWILIO_NUM")

today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = yesterday - dt.timedelta(days=1)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = os.environ.get("ALPHA_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stock_api_key
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_closing_price = float(stock_data["Time Series (60min)"][f"{yesterday} 20:00:00"]["4. close"])
day_before_yesterday_closing_price = float(stock_data["Time Series (60min)"][f"{day_before_yesterday} 20:00:00"]["4. close"])

difference = (yesterday_closing_price - day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

difference = abs(difference)
percentage_difference = round((difference/day_before_yesterday_closing_price)*100)

if percentage_difference > 5:
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    news_api_key = os.environ.get("NEWS_API_KEY")
    news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    three_articles = response.json()["articles"][:3]
    article_list = [f"{STOCK}: {up_down}{percentage_difference}%\nHeadline: {article_num['title']} \nURL: {article_num['url']}" for article_num in three_articles]

    client = Client(account_sid, auth_token)

    for article in article_list:
        message = client.messages \
            .create(
            body=article,
            from_=twilio_phone_number,
            to='+447706371382'
        )
        print(message.status)



