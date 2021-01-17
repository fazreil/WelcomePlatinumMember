from keep_alive import keep_alive
import discord
import os
import random
import corona
import movie

client = discord.Client()

ack_words = ["ok", "baik", "orait", "roger", "aye aye", "affirmative", "okie-dokie", "okie-doke"]

def get_random_ack():
  return(random.choice(ack_words))

def get_last_word(message):
  words = message.split()
  return(str(words[-1]))

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if 'bal' in message.content:
    await message.channel.send(get_random_ack()+" "+message.author.name)
    if 'corona' in message.content:
      await message.channel.send(corona.get_corona_update())
    elif 'movie' in message.content:
      movie_query = get_last_word(message.content)
      movie_list = movie.get_movie(movie_query)
      await message.channel.send(movie_list)
    else:
      await message.channel.send('Ye '+message.author.name+' apa boleh sy bantu?')
  
keep_alive()
client.run(os.getenv('TOKEN'))

