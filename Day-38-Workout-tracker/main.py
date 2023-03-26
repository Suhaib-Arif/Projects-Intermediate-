import requests
import os
import datetime

CONTINUE= True

while CONTINUE:
    operation=input("\nWhat operation do you want to do?\n1.Read data(READ)\n2.Add data(ADD)\n3.exit(EXIT)\n").upper()
    if operation == "READ":
        sheet_endpoint_get = os.environ["SHEET_GET"]

        headers = {
            "Authorization": os.environ["AUTHOURIZATION"],
            "Content-Type": "application/json"
        }

        sheet_response = requests.get(url=sheet_endpoint_get, headers=headers)
        sheet_response.raise_for_status()
        result = sheet_response.json()
        print("S.no\tDate\tTime\tExercise\tDuration\tCalories")
        for item in result["workouts"]:
            print(f"{item['id']}\t{item['date']}\t{item['time']}\t{item['exercise']}\t{item['duration']}\t{item['calories']}")

    elif operation == "ADD":
        headers={
            "x-app-id":os.environ["APP_ID"],
            "x-app-key":os.environ["USER_KEY"],
            "x-remote-user-id":"0"
        }
        parameters={
         "query":input("Tell me what exercises you did ?\n"),
         "gender":"male",
         "weight_kg":os.environ["WEIGHT"],
         "height_cm":os.environ["HEIGHT"],
         "age":20
        }
        exersice_endpoint = os.environ.get("EXERCISE_ENDPOINT")

        exercise_response=requests.post(url=exersice_endpoint, json=parameters, headers=headers)
        exercise_response.raise_for_status()
        result=exercise_response.json()

        Exerscise=str(result["exercises"][0]['name']).title()
        Duration=str(result["exercises"][0]['duration_min'])
        Calories=str(result["exercises"][0]['nf_calories'])

        print(f"EXERCISE: {Exerscise}\nDURATION: {Duration}\nCALORIES: {Calories}")

        time=datetime.datetime.now()
        Date=time.strftime("%Y/%m/%d")
        Time=time.strftime("%H:%M:%S")

        workout_data={
            "workout":
                {
                    "date":Date,
                    "time":Time,
                    "exercise":Exerscise,
                    "duration":Duration,
                    "calories":Calories,
                }
        }

        headers = {
            "Authorization": os.environ["AUTHOURIZATION"],
            "Content-Type": "application/json"
        }

        sheet_endpoint_post=os.environ["SHEET_POST"]
        sheet_response_post=requests.post(url=sheet_endpoint_post, json=workout_data, headers=headers)
        sheet_response_post.raise_for_status()
    else:
        CONTINUE=False
