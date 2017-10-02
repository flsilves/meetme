import json

import requests


# TODO add logging service
# TODO rename Meeting to Record
# TODO change recording attribute to storage_url
# TODO unit test
# TODO apply OOP
# TODO Pretty methods

class ClientAPI:
    def __init__(self, host_address):
        self.host_address = host_address
        self.meetings_url = self.host_address + "/meetings"
        self.users_url = self.host_address + "/users"
        self.json_header = {'Content-type': 'application/json'}

    def create_user(self, user_name, user_email):
        data = {"email": user_email, "name": user_name}
        return requests.post(self.meetings_url, data=json.dumps(data), headers=self.json_header)

    def get_all_users(self):
        return requests.get(self.users_url).json()

    def delete_user(self, user_email):
        user_list = self.get_all_users()
        user_to_delete = self.search(user_list, 'email', (user_email,))
        if not user_to_delete:
            print("DELETE USER: User {} does not exist\n".format(user_email))
            return 404
        id_to_delete = str(user_to_delete[0]['id'])
        response = requests.delete(self.users_url + "/" + id_to_delete, headers=self.json_header)
        return response.status_code

    def create_meeting(self, owner_id, recording_url, privacy):
        data = {"owner_id": owner_id, "recording": recording_url, "privacy": privacy}
        return requests.post(self.meetings_url, data=json.dumps(data), headers=self.json_header)

    def delete_meeting(self, meeting_id):
        return 0

    def share_meeting(self, meeting_id, user_email):
        return 0

    def create_user(self, user_name, user_email):
        data = {"email": user_email, "name": user_name}
        return requests.post(self.users_url, data=json.dumps(data), headers=self.json_header)

    @staticmethod
    def search(self, json_data, key, value):
        return list(filter(lambda f: f[key] in value, json_data))


if __name__ == '__main__':
    client = ClientAPI(host_address="http://127.0.0.1:5000")
    client.create_user("Flavio", "flaviosilvestre89@gmail.com")
    client.create_user("Ines Silva", "ines_silva@gmail.com")
    print(client.get_all_users())
    # delete_user("ines_silva@gmail.com")
    # print(get_all_users())
    client.create_meeting("1", "https://s3.amazonaws.com/meeting/393217", "Private")
    delete_user("flaviosilvestre89@gmail.com")
