import requests
from datetime import datetime

now = datetime.now()

current_date = now.strftime('%Y/%m/%d')
current_time = now.strftime('%H:%M:%S')

NUTR_API = "6d7045ce02bed78b191c186617656b3d"
APP_ID = "949d48e2"
data = str(input("How much you excersied today: "))
header={
    "x-app-id": APP_ID,
    "x-app-key": NUTR_API

}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

param={
    "query":data,
    "gender":"male",
    "weight_kg":67,
    "height_cm":170,
    "age":19
}

response = requests.post(url=endpoint, json= param, headers=header)
result = response.json()

sheet_url = "https://api.sheety.co/d931a0b910c42e5dfe649ea2e26eb52b/myWorkouts/workouts"
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response_data = requests.post(url=sheet_url,json = sheet_inputs)

print(response_data.text)
