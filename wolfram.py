import requests
import os

url = "https://api.wolframalpha.com/v1/result"

async def ask(msg, message):
  querystring = {"i":msg, "appid":os.getenv('WOLFRAM')}
  response = requests.get(url, params=querystring)
  await message.channel.send("```"+response.text+"```")