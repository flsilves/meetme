# Project Name
Build Status: [![Build Status](https://travis-ci.org/flsilves/meetme.svg?branch=master)](https://travis-ci.org/flsilves/meetme)

## *Installing Requirements*
```shell
$ pip install -r requirements.txt
```


## URI Summary

The following table summarises all the available resource URIs, and the effect of each verb on them. Each of them is relative to the base URI.

| Resource                                                                       | GET                                                               | POST                                  | PUT                                  | DELETE                                      |
| -----------------------------------------------------                          | ---------------------------------------------------               | ------------------------------------- | ---------------------------------    | ------------------------------------------- |
| [/users](#user)                                                                | Returns the list of all users registered                          | Create a new user(s)                  | N/A                                  | N/A                                         |
| [/users/:user\_id](#user)                                                     | Returns the details of a single reader                            | N/A                                   | N/A                                  | Deletes user                                |
| [/recordings/](#recording)                                                     | Returns the list of all recordings                                | Create a new recording(s)             | N/A                                  | N/A                                         |
| [/recordings/:recording\_id](#recording)                                      | Returns the info of a single recording                            | N/A                                   | N/A                                  | Deletes recording                           |
| [/users/:user\_id/permissions](#permission)                                   | Gets all recordings that {user\_id} has access to                 | N/A                                   | N/A                                  | N/A                                         |
| [/users/:user\_id/permissions/:recording\_id](#permission)                   | Queries if a particular {user\_id} has access to {recording\_id}  | N/A                                   | Creates a new permission for a user  | Remove permissions from user                |                                   |

## Message Summary

### User
``` json
{
    'id': Integer,
    'name': String,
    'email': String,
}
```
### Recording

## *DB Schema layout* 
![alt text](https://raw.githubusercontent.com/flsilves/meetme/master/imgs/layout.png)
