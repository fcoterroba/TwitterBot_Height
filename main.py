#!/usr/bin/python

# Import all the necesary packages
import tweepy
import json
import requests
import os
import random

def tweet():

  # Open the JSON file only with read permissions
  with open("characters.json", "r") as f:
    data = json.loads(f.read())
    
  # Authenticate to Twitter
  auth = tweepy.OAuthHandler("WRITE YOUR API KEYS HERE", "WRITE YOUR API KEYS HERE")
  auth.set_access_token("WRITE YOUR API KEYS HERE", "WRITE YOUR API KEYS HERE")
  
  # Create API object
  api = tweepy.API(auth)
  
  # Generate random character to tweet, check the appear value,
  # pick a random character of the JSON and finish changing 
  # appear's value to True for what don't appear never more
  character = 0
  while data[character]['appear`] == "True":
    character = int(random.uniform(0,len(data)))
    if data[character]['appear'] == "False":
      data[character]['appear'] = "True"
      break

  # Open again JSON but this time with write permission
  with open("characters.json", "w") as f:
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    
  # Transform, in a variable, meters to foots
  height_in_foot = round(float(data[character]['height'][0:4]) * 3.281, 3)
  
  # Save the final message (tweet)
  msg = f"RT si mides más que {data[character]['name']} --> {data[character]['height']}\nFAV si mides menos :(\n\nRT if you're taller than {data[character]['name']} --> {height_in_foot} ft\nFAV if you're smaller :("
  
  # Download the picture
  filename = "temp.jpg"
  request = requests.get(data[character]['img'], stream=True)
  if request.status.code == 200:
    with open(filename, 'wb') as image:
      for chunk in request:
        image.write(chunk)
        
  # Tweet the final result and then, supreme the picture
  api.update_with_media(filename, msg)
  os.remove('temp.jpg')
  
if __name__ == '__main__':
  tweet()
