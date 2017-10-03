import json
import requests


class ClientAPI:
    def __init__(self, host_address):
        self.host_address = host_address
        self.recordings_url = self.host_address + '/recordings'
        self.users_url = self.host_address + '/users'
        self.json_header = {'Content-type': 'application/json'}

    def create_user(self, user_name, user_email):
        data = {'email': user_email, 'name': user_name}
        return requests.post(self.recordings_url, data=json.dumps(data), headers=self.json_header)

    def get_all_users(self):
        return requests.get(self.users_url).json()

    def get_all_recordings(self):
        return requests.get(self.recordings_url).json()

    def create_user(self, user_name, user_email):
        data = {'email': user_email, 'name': user_name}
        return requests.post(self.users_url, data=json.dumps(data), headers=self.json_header)

    def delete_user(self, user_id):
        response = requests.delete(self.users_url + '/' + user_id, headers=self.json_header)
        return response.status_code

    def create_recording(self, owner_id, storage_url, password):
        data = dict(owner_id=owner_id, storage_url=storage_url, password=password)
        return requests.post(self.recordings_url, data=json.dumps(data), headers=self.json_header)

    def delete_recording(self, recording_id):
        url = self.recordings_url + '/' + recording_id
        return requests.delete(url, headers=self.json_header)

    def share_recording(self, user_id, recording_id):
        url = self.users_url + '/' + user_id + '/permissions/' + recording_id
        data = dict(user_id=user_id, recording_id=recording_id)
        return requests.put(url, data=json.dumps(data), headers=self.json_header)

    def unshare_recording(self, user_id, recording_id):
        url = self.users_url + '/' + user_id + '/permissions/' + recording_id
        return requests.delete(url, headers=self.json_header)


if __name__ == '__main__':
    client = ClientAPI(host_address='http://127.0.0.1:5000')

    client.create_user('Flavio', 'flaviosilvestre89@gmail.com')  ## Usage example
    client.create_user('User Foo', 'user@gmail.com')
    client.create_recording(owner_id='1', storage_url='https://s3.amazonaws.com/recording/393217',
                            password='secrethash')
    client.share_recording('2', '1')
    client.unshare_recording('2', '1')
    client.delete_recording('1')
    client.delete_user('1')
    client.create_recording(owner_id='2', storage_url='https://s3.amazonaws.com/recording/123', password='secrethash2')
    print(client.get_all_users())
    print(client.get_all_recordings())
