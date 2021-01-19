from keep_alive import keep_alive
import discord
import os
import random
import corona
import movie
import solat
import cuti

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

  msg = message.content.lower()

  if 'bal' in msg:
    await message.channel.send(get_random_ack()+" "+message.author.name)
    if 'corona' in msg:
      await message.channel.send(corona.get_corona_update())
    elif 'movie' in msg:
      movie_query = movie.get_movie_query(msg)
      movie_list = movie.get_movie(str(movie_query))
      await message.channel.send(movie_list)
    elif 'solat' in msg:
      await message.channel.send(solat.get_solat_time())
    elif 'cuti' in msg:
      for messages in cuti.get_cuti(get_last_word(msg)):
        await message.channel.send(messages)
    else:
      help_msg = 'Ye '+message.author.name+' apa boleh sy bantu? keyword: '
      help_msg = help_msg + '\n*corona* - kalau nak tau statistic harini'
      help_msg = help_msg + '\n*movie* <keywords> - kalau nak aku search movie based on keyword[s]'
      help_msg = help_msg + '\n*solat* - kalau nak aku aku lookup waktu solat KL'
      help_msg = help_msg + '\n*cuti* <bulan dalam integer> - aku list down cuti dalam bulan tu, default to current month'
      await message.channel.send(help_msg)
  
keep_alive()
client.run(os.getenv('TOKEN'))

