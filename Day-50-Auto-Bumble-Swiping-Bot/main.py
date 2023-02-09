from selenium import webdriver
import time
import os

url = "https://bumble.com/get-started"
email = os.environ.get("EMAIL")
password = os.environ.get("PW")

chrome_driver_path = "/Users/denisechan/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
#Delay to load page
time.sleep(10)

#Login to bumble
#Delay to accept cookies
time.sleep(10)
#Press login with fb
continue_with_fb = driver.find_element(by="css selector", value=".color-provider-facebook")
continue_with_fb.click()
#Delay to load pop up browser
time.sleep(10)
#Establish base and fb login windows
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
#Switch to fb login window
driver.switch_to.window(fb_login_window)
#Delay to accept cookies
time.sleep(10)
#Type login details
email_field = driver.find_element(by="css selector", value="#email")
email_field.send_keys(email)
pw_field = driver.find_element(by="css selector", value="#pass")
pw_field.send_keys(password)
login_button = driver.find_element(by="css selector", value="#loginbutton")
login_button.click()
#Delay for browser to process login
time.sleep(15)
#Switch back to base window
driver.switch_to.window(base_window)

#Pass on people for 3 mins
three_min = time.time() + 60*3
while True:
    time.time()
    #Press pass for someone
    pass_button = driver.find_element(by="css selector", value=".encounters-action--dislike")
    pass_button.click()
    #Load next profile
    time.sleep(3)
    if time.time() > three_min:
        break

driver.quit()