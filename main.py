from keep_alive import keep_alive
import discord
import os
import corona
import movie
import solat
import cuti
import utility_shorties as us
import praise
import maksud
import wolfram

client = discord.Client()

ack_words = ["ok", "baik", "orait", "roger", "aye aye", "affirmative", "okie-dokie", "okie-doke", ":thumbsup:", ":+1:", ":thumbup:", ":eyes:", ":100:"]
maksud_keywords = ["maksud","meaning","translate","alih"]

def is_bal_in(message):
  words = list(message.split(" "))
  for word in words:
    if(word == "bal"):
      return True
  return False

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.lower()

  if is_bal_in(msg):
    await message.channel.send(us.get_random(ack_words)+" "+message.author.name)
    if 'corona' in msg:
      await message.channel.send(corona.get_corona_update())
    elif 'movie' in msg:
      movie_query = movie.get_movie_query(msg)
      movie_list = movie.get_movie(str(movie_query))
      await message.channel.send(movie_list)
    elif 'solat' in msg:
      await message.channel.send(solat.get_solat_time())
    elif 'cuti' in msg:
      for messages in cuti.get_cuti(us.get_last_word(msg)):
        await message.channel.send(messages)
    elif 'praise' in msg:     
      await praise.prepare_praise(msg, message, client)
    elif us.keyword_in(maksud_keywords,msg):
      msg_wo_bal = us.filter(msg,['bal','iqbal'])
      msg_wo_bal_kw = us.filter(us.list_to_string(msg_wo_bal),maksud_keywords)
      await maksud.translate(msg_wo_bal_kw, message)
    elif '?' in msg:
      msg_wo_bal = us.list_to_string(us.filter(msg,['bal']))
      translated = await maksud.translate_string(msg_wo_bal)
      await wolfram.ask(translated, message)
    else:
      help_msg = 'Ye '+message.author.name+' apa boleh sy bantu? keyword: '
      help_msg = help_msg + '\n*corona* - kalau nak tau statistic harini'
      help_msg = help_msg + '\n*movie* <keywords> - kalau nak aku search movie based on keyword[s]'
      help_msg = help_msg + '\n*solat* - kalau nak aku aku lookup waktu solat KL'
      help_msg = help_msg + '\n*cuti* <bulan dalam integer> - aku list down cuti dalam bulan tu, default to current month'
      help_msg = help_msg + '\n*praise* <mention sorg user> - aku puji sikit user tu, xbanyak, sikit ja'
      help_msg = help_msg + '\n*maksud, meaning, translate, alih* <frasa bahasa melayu> - aku translate jadi en-US'
      help_msg = help_msg + '\n suffix *?* - nanti aku cari jawapan soalan korg, insya Allah'
      await message.channel.send(help_msg)
  
keep_alive()
client.run(os.getenv('TOKEN'))

