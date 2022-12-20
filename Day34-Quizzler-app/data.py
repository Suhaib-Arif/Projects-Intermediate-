# question_data =

import requests

data=requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")

unorganized_question_data=data.json()

question_data=unorganized_question_data["results"]
