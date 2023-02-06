import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml

# Scrap keyboard's price
url = "https://www.amazon.co.uk/LOGITECH-DEVICES-GRAPHITE-2-4GHZ-CENTRAL/dp/B07W6GVT3X/ref=sr_1_6?crid=3BTWE9A7T2MV2&keywords=Logitech+ERGO+K860&qid=1675685827&s=computers&sprefix=logitech+ergo+k860%2Ccomputers%2C306&sr=1-6"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(url=url, headers=headers)
contents = response.content

soup = BeautifulSoup(contents, "lxml")

whole_price = float(soup.select_one(selector=".a-price-whole").getText())
fraction_price = float(soup.select_one(selector=".a-price-fraction").getText())/100
price = whole_price + fraction_price

# Send email when keyboard's price is below £150
target_price = 150
if price <= target_price:
    product_title = soup.select_one(selector="#productTitle").getText().strip()
    import smtplib
    import os
    my_email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    message = f"{product_title} is now below £{target_price}, selling at £{price}\n{url}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        #Make connection secure and encrypts email
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
            .encode('utf-8')
        )


