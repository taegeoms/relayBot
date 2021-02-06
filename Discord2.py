import discord
from discord.ext import commands
import asyncio
import telepot 
from telepot.loop import MessageLoop
import time
import json


telegram_token = '1472069887:AAGqI2csyTUzCPbsRlXyrGC00RaNGaG_1n4'
bot = telepot.Bot(telegram_token)
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message)
    # channelID = str(message.channel.id)
    # f= open('relayDiscord.json')
    # data = json.load(f)
    # for x in data:
    #     if data[x]["source"] == channelID:
    #         print(message.attachments)
    #         if message.attachments:
    #             if ".pdf" in message.attachments[0].filename:                    
    #                 bot.sendDocument(data[x]["dest"], message.attachments[0].url)
    #             else:
    #                 bot.sendPhoto(data[x]["dest"], message.attachments[0].url)
    #             print("done!")
    #         if message.content:
    #             bot.sendMessage(chat_id=data[x]["dest"], text=message.content)
    #             print("done!")

    # time.sleep(2)

    

client.run("MTQwOTExNzI4OTc5MzQ1NDA4.X-hWMA.z_ZivxZ6GFft7vmWY7-jD2aznWM",bot=False)
