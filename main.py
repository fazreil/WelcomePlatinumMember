from keep_alive import keep_alive
import discord
import os
import random
import corona
import movie
import solat

client = discord.Client()

ack_words = ["ok", "baik", "orait", "roger", "aye aye", "affirmative", "okie-dokie", "okie-doke", ":thumbsup:", ":+1:", ":thumbup:", ":eyes:", ":100:"]

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
      movie_query = movie.get_movie_query(message.content)
      movie_list = movie.get_movie(str(movie_query))
      await message.channel.send(movie_list)
    elif 'solat' in message.content:
      await message.channel.send(solat.get_solat_time())
    else:
      help_msg = 'Ye '+message.author.name+' apa boleh sy bantu? keyword: '
      help_msg = help_msg + '\n*corona* - kalau nak tau statistic harini'
      help_msg = help_msg + '\n*movie* - kalau nak aku search movie'
      help_msg = help_msg + '\n*solat* - kalau nak aku aku lookup waktu solat KL'
      await message.channel.send(help_msg)
  
keep_alive()
client.run(os.getenv('TOKEN'))

