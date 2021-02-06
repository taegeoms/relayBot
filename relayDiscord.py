from telethon.sync import TelegramClient
from telethon import TelegramClient, events
from telethon.tl.types import InputPeerChat
from telethon import functions, types
import json


relayName=input("Enter the relay name: ")
source = input("Enter soource id: ")
dest = input("Enter the dest id with @: ")

def write_json(data, filename='relayDiscord.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)



with open('relayDiscord.json') as json_file:
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
