import requests
import json

jsonheader = {'Content-type': 'application/json'}

def get_tasks():
    r = requests.get("http://127.0.0.1:5000/todos")
    dumpRequest(r)


def post_task():
    url = "http://127.0.0.1:5000/users"
    data = {"user_id": "1"}
    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=jsonheader)


def dumpRequest(request):
    print(request.headers)
    print(request.json())



if __name__ == '__main__':
    get_tasks()


