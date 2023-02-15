import os
from insta_follower import InstaFollower

CHROME_DRIVER_PATH = "/Users/denisechan/Development/chromedriver"
SIMILAR_ACCOUNT = "derek_tch"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PW")

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(username=USERNAME, password=PASSWORD)
bot.find_followers(similar_account=SIMILAR_ACCOUNT)
bot.follow()

bot.driver.quit()