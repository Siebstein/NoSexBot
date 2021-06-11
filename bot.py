# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:09:54 2021

@author: Onni
"""
import os
import discord
#import nest_asyncio
from dotenv import load_dotenv
from urllib.parse import urlparse
from deepdream import getdeepdream


#nest_asyncio.apply()


    


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Koodi: ", "https://discord.com/api/oauth2/authorize?client_id=852906538242801686&permissions=0&scope=bot")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    SEX = ["SEX", "SEx", "SeX", "sEX", "Sex", "sEx", "seX", "sex"]
    
    for sex in SEX:
        if sex in message.content:
            await message.channel.send("NO SEX!")

client.run(TOKEN)