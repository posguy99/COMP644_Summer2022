
import json
import requests

from mod_read_write import read_token
from mod_read_write import write_plain_text_file

# i found that you have to strip the trailing newline or the auto token is invalid
# i added an rstrip()

TOKEN_FILENAME = input("What is the name of your API TOKEN file? ")
TOKEN = read_token(TOKEN_FILENAME).rstrip('\n')

#configure the HTTP header request parameters for the api call

HEADERS = "Bearer " + TOKEN

# create the end point

URI = "https://webexapis.com/v1/rooms"

# call the request

resp = requests.get(URI, headers={"Authorization":HEADERS})

# was the call successful
if resp.status_code != 200:
    print("Houston we have a problem")
    print(resp.status_code)

# call was successful
else:
    json_code = resp.json()
    print(json_code)

    # find information about a particular room
    ROOMID = "" # stores the room id
    ROOM_TO_FIND = input("What WebEx Room Id should be discovered? ")
    # "DevNet Summer 2022 T/Th"

    # walk the collection of rooms
    items = json_code["items"]
    for item in items:
        # print(item["id"])
        # print(item["title"])

        # was a match made
        if item["title"] == ROOM_TO_FIND:

            # found a matching room
            print("*** ROOM ***")
            print(item["title"])

            # the room id will be used later
            ROOMID = item["id"]
            ROOM_ID_FILE = input("What would you like to name your roomid file? ")
            write_plain_text_file(ROOM_ID_FILE, ROOMID)
            print(ROOMID)
            print("*"*20)

            break
            print("*"*20)
    else:
        print(f'No room was matched to {ROOM_TO_FIND}')
