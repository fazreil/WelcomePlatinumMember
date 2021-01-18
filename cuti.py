import requests
import json
import datetime
import pytz
import os

def format_time_to_my(time):
  kl = pytz.timezone('Asia/Kuala_Lumpur')
  return datetime.datetime.fromtimestamp(time,tz=kl).strftime("%H:%M")

def format_year_to_my(time):
  kl = pytz.timezone('Asia/Kuala_Lumpur')
  return datetime.datetime.fromtimestamp(time,tz=kl).strftime("%Y")

def format_month_to_my(time):
  kl = pytz.timezone('Asia/Kuala_Lumpur')
  month = datetime.datetime.fromtimestamp(time,tz=kl).strftime("%m")
  if(int(month)<10):
    month = month[1:]
  return month 

def convert_date(holiday_date):
  day = holiday_date['day']
  month = holiday_date['month']
  year = holiday_date['year']
  returnedDate = str(day)+"/"+str(month)+"/"+str(year)
  
  return returnedDate

def convert_type(holiday_type):
  return ", ".join(holiday_type)

def get_cuti(month):
  now = datetime.datetime.now().timestamp()
  try:
    if(int(month)<1 or int(month)>12):
      return ["letak la month tu betul2, haih"]
  except:
    month = format_month_to_my(now)
  request_url = "https://calendarific.com/api/v2/holidays?api_key="+os.getenv('CALENDARIFIC_KEY')+"&country=MY&year="+format_year_to_my(now)
  response = requests.get(request_url)
  json_data = json.loads(response.text)
  holidays = json_data['response']['holidays']
  messages = ["Ni cuti utk bulan "+str(month)]
  message = "```"

  for holiday in holidays:
    
    if(len(message)>=150):
      message = message + "```"
      messages.append(message)
      message = "```"

    if(('National holiday' in holiday['type']) or ('Common local holiday' in holiday['type'])):
      # print(holiday['name'])
      # print(month)
      # print(holiday['date']['datetime']['month'])
      if(str(month) == str(holiday['date']['datetime']['month'])):
        message = message + holiday['name'] +" - "+ convert_date(holiday['date']['datetime'])+" \n"

  message = message + "```"
  if(message != "``````"):
    messages.append(message)

  return(messages)