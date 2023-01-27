import requests
from datetime import datetime as dt
import json
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

GENDER = "female"
WEIGHT_KG = 57
HEIGHT_CM = 167
AGE = 28

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

exercise_params = {
    "query": input("Tell me which exercise you did today: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercise_data = exercise_response.text
#convert exercise data to a dict
exercise_data = json.loads(exercise_data)


USERNAME = "5b2a4377f68e31012fb839fad9f2e610"
PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"
SHEETY_TOKEN = os.environ.get("TOKEN")

today_date = dt.now().strftime(f'%Y/%m/%d')
today_time = dt.now().strftime(f'%H:%M:%S')
exercise = exercise_data["exercises"][0]['name']
duration = exercise_data["exercises"][0]['duration_min']
calories = exercise_data["exercises"][0]['nf_calories']

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

add_data_params = {
    "workout": {
    "date": today_date,
    "time": today_time,
    "exercise": exercise.title(),
    "duration": duration,
    "calories": calories
    }
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_TOKEN
}

sheety_resposne = requests.post(url=sheety_endpoint, json=add_data_params, headers=sheety_headers)
print(sheety_resposne.text)


