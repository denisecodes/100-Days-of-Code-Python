from selenium import webdriver
from selenium.webdriver import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_driver_path = "/Users/denisechan/Development/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # Wait for page to load
        time.sleep(10)
        cookies = self.driver.find_element(by="css selector", value="#onetrust-accept-btn-handler")
        cookies.click()
        # Wait for cookies to be accepted
        time.sleep(5)
        # Test internet speed
        test_speed = self.driver.find_element(by="css selector", value=".js-start-test")
        test_speed.click()
        # Wait for speed to be tested
        time.sleep(90)
        # Retrieve download and upload speeds
        self.down = float(self.driver.find_element(by="css selector", value=".download-speed").text)
        self.up = float(self.driver.find_element(by="css selector", value=".upload-speed").text)

    def tweet_at_provider(self, username, password):
        self.driver.get("https://twitter.com/i/flow/login")
        # Delay to load page
        time.sleep(5)
        email_field = self.driver.find_element(by="name", value="text")
        email_field.send_keys(username)
        next_button = self.driver.find_element(by="xpath", value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_button.click()
        # Delay to process username
        time.sleep(5)
        password_field = self.driver.find_element(by="xpath", value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        # Delay to process login
        time.sleep(10)
        self.tweet_field = self.driver.find_element(by="css selector", value="br[data-text='true']")
        time.sleep(3)
        self.tweet_button = self.driver.find_element(by="xpath", value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")







