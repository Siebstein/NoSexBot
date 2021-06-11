# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:09:54 2021

@author: Onni
"""
import os
import discord
import re
from dotenv import load_dotenv

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
    
    msg = message.content
    SEX = ["SEX", "SEx", "SeX", "sEX", "Sex", "sEx", "seX", "sex"]
    
    SEXExp = "(?i)((?<!no )[s][e€£][x](?!\S))|(\A([S][e€£][x]))"
    
    contains = re.search(SEXExp, msg)
    
    """
    for sex in SEX:
        if sex in message.content:
            await message.channel.send("NO SEX!")
    """
    
    if contains:
        await message.channel.send("NO SEX!")

client.run(TOKEN)