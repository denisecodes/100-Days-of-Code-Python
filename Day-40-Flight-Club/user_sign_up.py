import requests
import os

sheety_post_endpoint = os.environ.get("SHEETY_POST_ENDPOINT")
sheety_token = os.environ.get("SHEETY_TOKEN")

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": sheety_token
}

print("Welcome to Denise's Flight Club.\nWe find the best flight deals and email you")


first_name = input(f"What is your first name?\n").title()
last_name = input(f"What is your last name?\n").title()

is_email_correct = False
while is_email_correct == False:
  email = input(f"What is your email?\n")
  email_confirm = input(f"Type your email again.\n")
  if email == email_confirm:
    is_email_correct = True
  else:
    print("The email confirmation does not match, please input your email again!")

add_user_params = {
  "user": {
    "firstName": first_name,
    "lastName": last_name,
    "email": email_confirm
  }
}

response = requests.post(url=sheety_post_endpoint, json=add_user_params, headers=sheety_headers)

print("Success, your email has been added and you're in the club!")
