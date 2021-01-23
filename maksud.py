import os
import requests
import json

url = "https://nlp-translation.p.rapidapi.com/v1/translate"

def fetch_translation(msg,to_lang,from_lang):
  querystring = {"text":msg, "to":to_lang, "from":from_lang}
  headers = {
    'x-rapidapi-key': ""+os.getenv('RAPIDAPI'),
    'x-rapidapi-host': "nlp-translation.p.rapidapi.com"
    }

  response = requests.get(url, headers=headers, params=querystring)
  json_data = json.loads(response.text)
  translated = str(json_data['translated_text'][to_lang])
  
  return translated

async def translate(msg,message):
  query = " ".join(msg)
  await message.channel.send("```"+fetch_translation(query,"en","my")+"```")

async def translate_string(msg):
  translated_query = fetch_translation(msg,"en","my")
  return translated_query
