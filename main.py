import requests
from datetime import datetime
# https://docx.syndigo.com/developers/docs/understand-request-headers
# https://docx.syndigo.com/developers/docs/natural-language-for-exercise
# https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise

GENDER = " "
WEIGHT_KG = " "
HEIGHT_CM = " "
AGE = " "

APP_ID = " "
API_KEY = " "

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

sheet_endpoint = "https://api.sheety.co/99c48ac7041ab94d119738752ac9f9f0/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

