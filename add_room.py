
# session 06-23-22

import requests
import json

from mod_read_write import read_token
from mod_read_write import read_plain_text_file
from mod_read_write import write_plain_text_file

#get the token from a file

TOKEN_FILENAME = input ("What is the name of your API TOKEN file? " )

TOKEN = read_token(TOKEN_FILENAME).rstrip('\n')

HEADERS = 'Bearer '+ TOKEN

#content-type is the encoding http request payload header
CONTENT_TYPE = "application/json"

#create the body parameter

#New room title
ROOM_TITLE = input("What is the title of your new room? " )
BODY = json.dumps({
    "title": ROOM_TITLE,
    "isLocked": True
})

URI = "https://webexapis.com/v1/rooms"

resp = requests.post(URI, \
headers={
    "Authorization" :HEADERS,
    "Content-Type": CONTENT_TYPE
    }, data=BODY)

print (f'HTTP Response Code {resp.status_code}' )
print ("*"*20)

if resp.status_code > 199 or resp.status_code < 300:
#a successful api call has completed
    json_code = resp.json()
    ROOMID = json_code["id"]
    FILENAME = input ("What would you like your new roomId file saved as? ")
    write_plain_text_file(FILENAME, ROOMID)
    print (f'Your roomId is has been written to: {FILENAME}')
else:
    #api call failed
    print ("Houston we have a problem")
