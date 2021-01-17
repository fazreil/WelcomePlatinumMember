import requests
import json

def get_corona_update():
  response = requests.get("https://corona.lmao.ninja/v2/countries/MY?strict=true&query")
  json_data = json.loads(response.text)
  todayCase = str(json_data['todayCases'])
  todayRec = str(json_data['todayRecovered'])
  todayDeaths = str(json_data['todayDeaths'])
  corona_update = "Today Cases:"+todayCase+"\nToday Recovered:"+todayRec+"\ntoday Death:"+todayDeaths
  return(corona_update)