from telethon.sync import TelegramClient 
from telethon import TelegramClient,events
from telethon.tl.types import InputPeerChat
from telethon import functions, types
import json

# first step is to install requrments
# pip install telethon


# get your api_id, api_hash, token 
# from telegram https://my.telegram.org/
api_id = ''
api_hash = ''

# your phone number
phone = "+14755229513"

   
client = TelegramClient('session', api_id, api_hash) 
   
client.connect() 
    
if not client.is_user_authorized(): 
   
    client.send_code_request(phone) 
      
    # signing in the client 
    client.sign_in(phone, input('Enter the code: '))     


@client.on(events.NewMessage)
async def my_event_handler(event):
    print("Start")
    words = open("words.txt", "r")
    channelID = str(event.message.chat_id)
    f= open('relay.json')
    data = json.load(f)
    for x in data:
        try:
            if data[x]["source"] == channelID:
                for line in words:
                    stripped_line = line.strip() 
                    event.message.message = event.message.message.replace(stripped_line,"")                    
                await client.send_message(data[x]["dest"], event.message)  
                print("Done!\n")

        except Exception as identifier:
            print(identifier)
    print("End")

client.start()
client.run_until_disconnected()
    

