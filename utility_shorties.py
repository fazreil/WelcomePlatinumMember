import random

def get_random(words):
  return(random.choice(words))

def get_last_word(message):
  words = message.split()
  return(str(words[-1]))

def is_word_in(keyword, words):
  for word in words:
    if(keyword == word):
      return True
  return False

def filter(message, filter_words):
  words = list(message.split(" "))
  returnWords = []
  for word in words:
    if(not is_word_in(word,filter_words)):
      returnWords.append(word)
  return returnWords

def keyword_in(keywords,message):
  message_list = message.split()
  for keyword in keywords:
    for word in message_list:
      if(keyword == word):
        return True
  return False

def list_to_string(list):
  return " ".join(list)