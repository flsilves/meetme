# meetme [![Build Status](https://travis-ci.org/flsilves/meetme.svg?branch=master)](https://travis-ci.org/flsilves/meetme) 
Simple meeting management REST API **(python 3.6)**

## **Deployment steps**
### 1. Install Requirements
```shell
$ pip install -r requirements.txt
```
### 2. Create Database model
```shell
$ python models.py
```
### 3. Run REST api
``` shell
$ python app.py
```

## URI Summary

The following table summarises all the available resource URIs, and the effect of each verb on them. Each of them is relative to the base URI.

| Resource                                                                       | GET                                                               | POST                                  | PUT                                  | DELETE                                      |
| -----------------------------------------------------                          | ---------------------------------------------------               | ------------------------------------- | ---------------------------------    | ------------------------------------------- |
| [/users](#user)                                                                | Returns the list of all users registered                          | Create a new user(s)                  | N/A                                  | N/A                                         |
| [/users/:user\_id](#user)                                                     | Returns the details of a single reader                            | N/A                                   | N/A                                  | Deletes user                                |
| [/recordings/](#recording)                                                     | Returns the list of all recordings                                | Create a new recording(s)             | N/A                                  | N/A                                         |
| [/recordings/:recording\_id](#recording)                                      | Returns the info of a single recording                            | N/A                                   | N/A                                  | Deletes recording                           |
| [/users/:user\_id/permissions](#permissions)                                   | Gets all recordings that {user\_id} has access to                 | N/A                                   | N/A                                  | N/A                                         |
| [/users/:user\_id/permissions/:recording\_id](#permissions)                   | Queries if a particular {user\_id} has access to {recording\_id}  | N/A                                   | Creates a new permission for a user  | Remove permissions from user                |                                   |

## Resources Properties
### User
Field | Data Type | Description
--- | --- | ---
id | integer | Unique identifier
name | string | User name
email | string | User email (must be unique)


### Recording
Field | Data Type | Description
--- | --- | ---
id | integer | Unique identifier
owner_id | integer | Identifier of the user that owns the recording (host)
storage_url | string | URL to the recording video
password | string | Password required to access the recording

### Permissions
Field | Data Type | Description
--- | --- | ---
user_id| integer | A user that isn't the owner of the recording
recording_id | string | The recording identifier that has been granted access to

## Run Unit tests
```shell
$ python tests.py
```
Results for current build here: https://travis-ci.org/flsilves/meetme

## *DB Schema layout* 
![alt text](https://raw.githubusercontent.com/flsilves/meetme/master/imgs/layout.png)
