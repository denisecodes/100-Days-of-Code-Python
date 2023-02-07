from selenium import webdriver
import time

chrome_driver_path = "/Users/denisechan/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by="id", value="cookie")
timeout = time.time() + 5
three_min = time.time() + 60*3

# Get hold of items
items = driver.find_elements(by="css selector", value="#store div")
# Get hold of item ids
item_ids = [item.get_attribute("id") for item in items]

game_is_on = True
while game_is_on:
    cookie.click()
    if time.time() > timeout:
        # Get hold of item prices
        item_prices = []
        all_prices = driver.find_elements(by="css selector", value="#store b")
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        # Put together item ids together with their item prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        # Get hold of num of cookies
        cookie_counter = driver.find_element(by="id", value="money").text.strip()
        if "," in cookie_counter:
            cookie_counter = cookie_counter.replace(",", "")
        cookie_counter = int(cookie_counter)
        # Store upgrades that we can currently afford into a dictionary
        affordable_upgrades = {}
        # Put affordable cost and id into a tuple inside a list
        for cost, id in cookie_upgrades.items():
            if cookie_counter > cost:
                affordable_upgrades[cost] = id
        # Purchase the most expensive affordable upgrade
        highest_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_affordable_upgrade]
        #Click highest affordable upgrade
        purhcase_upgrade = driver.find_element(by="id", value=to_purchase_id)
        purhcase_upgrade.click()
        #Add another timeout
        timeout = time.time() + 5
    if time.time() > three_min:
        cookie_per_second = driver.find_element(by="id", value="cps").text
        print(cookie_per_second)
        game_is_on = False

driver.quit()