import discord
import os
import requests
import json
from replit import db
from keep_alive import keep_alive



Client =discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q'] +" -"+json_data[0]['a']
  return (quote)

#nicknames for some friends

rohan=["hadi","kale","kauwa","kaag"]
prasun=["lade","thule","prasun"]
saiyam=["yumyum","shyame","chame"]


@Client.event
async def on_ready(): 
  print('We have logged in as {0.user}'.format(Client))

@Client.event
async def on_message(message):
  if message.author==Client.user:
    return

  if message.content.startswith('Hello'):
    await message.channel.send('Hello! ')

  if message.content.startswith('#inspire'):
    quote=get_quote()
    await message.channel.send(quote)

  if message.content.startswith('Thanks'):
    await message.channel.send('You are welcome.') 

  if any (word in message.content for word in rohan):
    await message.channel.send('You must be talking about Mr.Rohan') 

  if any (word in message.content for word in prasun):
    await message.channel.send('He has the biggest ego in the world')

  if any (word in message.content for word in saiyam):
    await message.channel.send('Shhhhh!! Or he will kill you')   

keep_alive()
Client.run(os.getenv('TOKEN'))    


