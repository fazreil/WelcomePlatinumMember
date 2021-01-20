import random

def get_random(words):
  return(random.choice(words))

def get_last_word(message):
  words = message.split()
  return(str(words[-1]))