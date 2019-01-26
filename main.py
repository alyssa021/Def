from __future__ import print_function
from config import app_id, app_key
import requests
import json

language = 'en'
word_id = 'service'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

r_json = r.json();
contents = r_json["results"];

for content in contents:
  print("Word: " + content["id"]);
  lexicalEntries = content["lexicalEntries"];

  for lexicalEntry in lexicalEntries:
    entries = lexicalEntry["entries"]

    for entry in entries:
      senses = entry["senses"];

      for sense in senses:
        definitions = sense["definitions"];

        for definition in definitions:
          print("[o] " + definition);
