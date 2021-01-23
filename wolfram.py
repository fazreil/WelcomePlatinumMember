import requests
import os
import discord

url = "https://api.wolframalpha.com/v1/result"

def embed(string_to_embed):
  embeded_message = discord.Embed()
  embeded_message.set_footer(text=string_to_embed)
  return embeded_message

async def ask(msg, message):
  await message.channel.send("```Query: "+msg+"```")
  querystring = {"i":msg, "appid":os.getenv('WOLFRAM')}
  response = requests.get(url, params=querystring)
  await message.channel.send(content="```"+response.text+"```", embed=embed("Source: wolframalpha.com"))