
# session 06-23-22

import requests
import json

from mod_read_write import read_token
from mod_read_write import read_plain_text_file
from mod_read_write import write_plain_text_file

#get the token from a file

TOKEN_FILENAME = input ("What is the name of your API TOKEN file? " )
TOKEN = read_token(TOKEN_FILENAME).rstrip('\n')

HEADERS = 'Bearer ' + TOKEN

#get the roomId from a file
FILENAME = input("What is the roomld file? " )
ROOMID = read_plain_text_file(FILENAME)
ROOMID = ROOMID[0]

print(ROOMID)

#content-type is the encoding http request payload header
CONTENT_TYPE = 'application/json'

#New member
MEMBER = input("What is the email of the new member? ")

#create the body parameter

BODY = json.dumps({
    "roomId": ROOMID,
    "personEmail": MEMBER,
    "isModerator": True
})

#API call
URI = "https://webexapis.com/v1/memberships"

resp = requests.post(URI, \
    headers={
        "Authorization" : HEADERS,
        "ContentType": CONTENT_TYPE
        }, data=BODY)

print (f'HTTP Response Code {resp.status_code}')
print ("*"*20)

#process the response
if resp.status_code > 199 and resp.status_code < 300:
#a successful api call has completed
    json_code = resp.json()
    ADDED_MEMBER = json_code["personDisplayName"]
    print(f'Member added {ADDED_MEMBER}')
else:
    #api call failed
    print("Houston we have a problem")
    print(resp.text)

