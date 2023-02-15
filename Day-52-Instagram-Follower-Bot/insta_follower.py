from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstaFollower:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(executable_path=driver)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        #Delay to accept load page
        time.sleep(10)
        #Accept cookies
        cookies = self.driver.find_element(by="css selector", value="._a9_1")
        cookies.click()
        time.sleep(3)
        #Login
        username_field = self.driver.find_element(by="name", value="username")
        username_field.send_keys(username)
        password_field = self.driver.find_element(by="name", value="password")
        password_field.send_keys(password)
        login_button = self.driver.find_element(by="css selector", value="._acas")
        login_button.click()
        time.sleep(10)
        # Don't save login info
        save_login = self.driver.find_element(by="css selector", value="._ac8f button")
        save_login.click()
        time.sleep(5)
        #Turn off notifications
        notifications = self.driver.find_element(by="css selector", value="._a9_1")
        notifications.click()
        time.sleep(3)


    def find_followers(self, similar_account):
        #Find followers page
        self.driver.get(f"https://www.instagram.com/{similar_account}/followers")
        time.sleep(10)
        for i in range(10):
            followers_list = self.driver.find_element(by="css selector", value="._aano")
            # “arguments[0]” means first index of page starting at 0.
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_list)
            time.sleep(3)

    def follow(self):
        follow_buttons = self.driver.find_elements(by="css selector", value="._aano button")
        for button in follow_buttons:
            print(button.text)
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by="css selector", value="._a9_1")
                cancel_button.click()
                time.sleep(1)
    time.sleep(10)




