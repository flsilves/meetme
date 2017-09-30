import requests
import json

jsonheader = {'Content-type': 'application/json'}

def create_user(user_name, user_email):
    url = "http://127.0.0.1:5000/users"
    data = {"email": user_email, "name": user_name}
    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=jsonheader)

def delete_user(user_email):
    url = "http://127.0.0.1:5000/users/2"
    response = requests.delete(url, headers=jsonheader)
    print(response.status_code)


def create_meeting(owner, recording_url, privacy):
    url = "http://127.0.0.1:5000/meetings"
    data = {"owner": owner, "recording": recording_url, "privacy": privacy}
    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=jsonheader)
    dump(response)


def delete_meeting(meeting_id):
    return 0

def share_meeting(meeting_id, user_email):
    return 0


def get_all_users():
    r = requests.get("http://127.0.0.1:5000/users")
    dump(r)

def create_user(user_name, user_email):
    url = "http://127.0.0.1:5000/users"
    data = {"email": user_email, "name": user_name}
    response = requests.post(url, data=json.dumps(data), headers=jsonheader)
    dump(response)


def dump(message):
    for field in message:
        print(field.decode('utf-8'))


if __name__ == '__main__':
    get_all_users()
    delete_user("ines_silva@gmail.com")
    delete_user("flaviosilvestre89@gmail.com")
    #create_user("Flavio", "flaviosilvestre89@gmail.com")
    #create_user("Inês Silva", "ines_silva@gmail.com")

   # create_meeting("Flavio", "https://s3.amazonaws.com/meeting/393217", "Private")


