import discord
import time
from discord.ext import commands
import datetime
import base64
import requests
import os
from XSONotifications import XSOMessage, XSNotifier

# Intializes bot and it's options.
token = os.environ.get("TOKEN")
if token == None:
    print("token not set!\nuse: set TOKEN=insert_token_here\nwithout quotes!")
    exit()
prefix = '*'
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)

XSNotifier = XSNotifier()

@bot.event
async def on_ready():
    print(f"XSNotifications_discord is running.")

@bot.event
async def on_message(message):
    if (isinstance(message.channel, discord.channel.DMChannel) or bot.user in message.mentions) and message.author != bot.user: 
        msg = XSOMessage()
        msg.messageType = 1
        msg.sourceApp = "Discord"
        msg.opacity = 0.7
        msg.title = str(message.author) + " - " + msg_type
        msg.audioPath = ""
        msg.content = ""
        msg.useBase64Icon = True

        if message.channel.type == discord.ChannelType.private:
            msg_type = "DM"
        else:
            msg_type = message.guild.name
            # msg.content = message.channel.name + r"\u2028"

        msg.content += message.clean_content

        ava_url = ava_url.rsplit(".", 1)[0] + ".jpg"
        icon = base64.b64encode(requests.get(ava_url).content)
        msg.icon = icon.decode('utf-8')
        
        XSNotifier.send_notification(msg)

    
bot.run(token, bot=False)





