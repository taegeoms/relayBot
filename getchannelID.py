from telethon.sync import TelegramClient
from telethon import TelegramClient, events
from telethon.tl.types import InputPeerChat
from telethon import functions, types
import json

api_id = ''
api_hash = ''

# your phone number
phone = ""


client = TelegramClient('session', api_id, api_hash)

client.connect()

if not client.is_user_authorized():

    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))

relayName=input("Enter the relay name: ")
source = input("Enter soource link: ")
dest = input("Enter the dest id: ")

val = client.get_input_entity(source)
source ="-100"+str(val.channel_id)

def write_json(data, filename='relay.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)



with open('relay.json') as json_file:
    data = json.load(json_file)
    temp = data
    y = {relayName: {
        "source": source,
         "dest": dest,
         }
         }
    temp.update(y)

write_json(data)

# print(val)
