import praw
import discord
from datetime import datetime, time, timedelta
import asyncio
import os


clientid = os.environ['clientid']               #os.environ is from replit secret key
clientsecret = os.environ['clientsecret']       #This part only works in replit, would have to replace
name = os.environ['name']
passw = os.environ['pass']
agent = os.environ['agent']
token = os.environ['token']
channelid = int(os.environ['channelid'])

reddit = praw.Reddit(client_id  = clientid,          #logging into reddit account
                     client_secret = clientsecret,
                     username = name,
                     password = passw,
                     user_agent = agent)

user = reddit.redditor("ZenTori")
top = user.submissions.top("week")
client = discord.Client()


  

async def send_url():
    await client.wait_until_ready() # ensures cache is loaded
    channel = client.get_channel(channelid) 
    while True:
      user = reddit.redditor("ZenTori")  #Reddit user
      top = user.submissions.top("week")  #filter posts by top of the current week
      for item in top:
        name = item.title
        url = item.url
        emb = discord.Embed(title = name, description=url) #adds hyperlink to description to allow for users to click
        emb.set_image(url = url)
        emb.set_thumbnail(url = url)
        await channel.send(embed=emb)
      await asyncio.sleep(604800) #wait for 1 week / 604800 secs

@client.event
async def on_ready():
    client.loop.create_task(send_url()) 



client.run(os.getenv('token'))







