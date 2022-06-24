
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
