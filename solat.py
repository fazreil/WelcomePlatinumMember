import requests
import json
import datetime
import pytz

#time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))

def format_time_to_my(time):
  kl = pytz.timezone('Asia/Kuala_Lumpur')
  return datetime.datetime.fromtimestamp(time,tz=kl).strftime("%H:%M")

def get_solat_time():
  response = requests.get("http://mpt.i906.my/mpt.json?code=wlp-0&filter=1")
  json_data = json.loads(response.text)
  responses = json_data['response']
  subuh = responses['times'][0]
  syuruk = responses['times'][1]
  zohor = responses['times'][2]
  asar =  responses['times'][3]
  maghrib = responses['times'][4]
  isyak = responses['times'][5]
  
  kl = pytz.timezone('Asia/Kuala_Lumpur')
  today = datetime.datetime.fromtimestamp(subuh,tz=kl).strftime("%d-%m-%Y")
  message = "Ni waktu solat area KL untuk harini ("+today+")\n"
  message = message + "Subuh: "+format_time_to_my(subuh)+"\n"
  message = message + "Syuruk: "+format_time_to_my(syuruk)+"\n"
  message = message + "Zohor: "+format_time_to_my(zohor)+"\n"
  message = message + "Asar: " +format_time_to_my(asar)+"\n"
  message = message + "Maghrib: "+format_time_to_my(maghrib)+"\n"
  message = message + "Isyak: "+format_time_to_my(isyak)
  return(message)