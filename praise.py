import discord
import utility_shorties as us


praise_words = ["terbaik", "gempak", "sempoi lah", "marvellous", "good job", "tahniah", "super!", "magnificent", "congratulations", "bravo"]
praise_emojis = [":100:", ":thumbsup:", ":+1:"]

def praise(user):
  embeded_message = us.get_random(praise_words) + " " + user.mention + " " + us.get_random(praise_emojis)
  return embeded_message

def embed(user):
  embeded_message = discord.Embed()
  embeded_message.set_thumbnail(url=str(user.avatar_url))
  return embeded_message

async def prepare_praise(msg, message, client):
  if("@here" in msg):
    await message.channel.send("Sorry @here cannot "+message.author.name)
  elif("@everyone" in msg):
    await message.channel.send("Sorry @everyone cannot "+message.author.name)
  else:
    try:
      discord_id = us.get_last_word(msg)
      print(discord_id[3:-1])
      user = await client.fetch_user(discord_id[3:-1]) #desktop client
      await message.channel.send(content="**"+praise(user)+"**", embed=embed(user))
    except Exception as e:
      try:
        print(str(e))
        discord_id = us.get_last_word(msg)
        print(discord_id[2:-1])
        user = await client.fetch_user(discord_id[2:-1]) #mobile client
        await message.channel.send(content="**"+praise(user)+"**", embed=embed(user))
      except Exception as f:
        print(str(f))
        await message.channel.send("Sorry "+message.author.name+" siapa tu?")
