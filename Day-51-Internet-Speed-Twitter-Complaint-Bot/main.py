import os
from internet_speed_twitter_bot import InternetSpeedTwitterBot
from selenium import webdriver
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = os.environ.get("USERNAME")
TWITTER_PASSWORD = os.environ.get("PW")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(username=TWITTER_USERNAME, password=TWITTER_PASSWORD)
bot.tweet_field.send_keys(f"Hey Internet Provider, why is my internet speed {bot.down}down/{bot.up}up when I pay for "
                      f"{PROMISED_DOWN}down/{PROMISED_UP}up")
time.sleep(10)
bot.tweet_button.click()
time.sleep(10)

