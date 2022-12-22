import requests
import os
import datetime as dt
create_user_endpoint = "https://pixe.la/v1/users"

TOKEN = os.environ["TOKEN"]
USERNAME = os.environ["USERNAME"]
GRAPH_ID = os.environ["GRAPH_ID"]
GRAPH_NAME = os.environ["GRAPH_NAME"]

parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{create_user_endpoint}/{USERNAME}/graphs"

graph_config= {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "minutes",
    "type": "float",
    "color": "kuro"
}

headers={
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

time = dt.datetime.now()
time = time.strftime("%Y%m%d")


request_parameter = {
    "date": time,
    "quantity": input("How much did you procrastinate today?")

}

# get_graph_endpoint=f"{graph_endpoint}/{GRAPH_ID}"
"/v1/users/<username>/graphs/<graphID>"

update_graph_parameter={
    "quantity":"37.7"
}



# response = requests.post(url=get_graph_endpoint, json=request_parameter,headers= headers)
"/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>"

update_graph_endpoint=f"{create_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{time}"
# response = requests.put(url=update_graph_endpoint,json=update_graph_parameter,headers=headers)
# print(response.text)

delete_graph_endpoint=f"{create_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{time}"
requests.delete(url=delete_graph_endpoint,headers=headers)