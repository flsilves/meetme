import requests
import json

# TODO add logging service
# TODO rename Meeting to Record
# TODO change recording attribute to storage_url
# TODO unit test
# TODO apply OOP
# TODO Pretty methods
# Membership endpoint and API
json_header = {'Content-type': 'application/json'}

host_address = "http://127.0.0.1:5000"
meetings_url = host_address + "/meetings"
users_url = host_address + "/users"


def create_user(user_name, user_email):
    data = {"email": user_email, "name": user_name}
    return requests.post(meetings_url, data=json.dumps(data), headers=json_header)


def dump(message):
    for field in message:
        print(field.decode('utf-8'))


def copyf(data, key, allowed):
    return list(filter(lambda f: f[key] in allowed, data))


def get_all_users():
    return requests.get(users_url).json()


def delete_user(user_email):
    user_list = get_all_users()
    user_to_delete = copyf(user_list, 'email', (user_email,))
    if not user_to_delete:
        print("DELETE USER: User {} does not exist\n".format(user_email))
        return 404
    id_to_delete = str(user_to_delete[0]['id'])
    response = requests.delete(users_url + "/" + id_to_delete, headers=json_header)
    return response.status_code


def create_meeting(owner_id, recording_url, privacy):
    data = {"owner_id": owner_id, "recording": recording_url, "privacy": privacy}
    return requests.post(meetings_url, data=json.dumps(data), headers=json_header)


def delete_meeting(meeting_id):
    return 0


def share_meeting(meeting_id, user_email):
    return 0


def create_user(user_name, user_email):
    data = {"email": user_email, "name": user_name}
    return requests.post(users_url, data=json.dumps(data), headers=json_header)


if __name__ == '__main__':
    create_user("Flavio", "flaviosilvestre89@gmail.com")
    create_user("Ines Silva", "ines_silva@gmail.com")
    print(get_all_users())
    # delete_user("ines_silva@gmail.com")
    # delete_user("flaviosilvestre89@gmail.com")
    # print(get_all_users())
    create_meeting("1", "https://s3.amazonaws.com/meeting/393217", "Private")
