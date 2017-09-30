import requests
import json

jsonheader = {'Content-type': 'application/json'}

def create_user(user_name, user_email):
    url = "http://127.0.0.1:5000/users"
    data = {"email": user_email, "name": user_name}
    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=jsonheader)

def create_conference(owner, recording_url, privacy):
    return 0

def delete_conference(meeting_id):
    return 0

def share_meeting(meeting_id, user_email):
    return 0


def get_all(resource):
    r = requests.get("http://127.0.0.1:5000/" + resource)
    dumpRequest(r)

def create_user(user_name, user_email):
    url = "http://127.0.0.1:5000/users"
    data = {"email": user_email, "name": user_name}
    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=jsonheader)


def dumpRequest(request):
    print(request.headers)
    print(request.json())

if __name__ == '__main__':
    get_all("users")
    create_user("Flavio", "flaviosilvestre89@gmail.com")


