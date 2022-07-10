from dotenv import load_dotenv
import os

load_dotenv()
from fastapi import FastAPI
from marvel_connection import connect

app = FastAPI()

MARVEL_TS = os.environ["MARVEL_TS"]
MARVEL_APIKEY = os.environ["MARVEL_APIKEY"]
MARVEL_HASH = os.environ["MARVEL_HASH"]

params = f"ts={MARVEL_TS}&apikey={MARVEL_APIKEY}&hash={MARVEL_HASH}"

@app.get("/searchComics/")
async def search_comics(name: str = None):
    if name:
      character = get_character(name)
      if character:
        return character
      else:
        comic = get_comic(name)
        return comic
    else:
      characters = get_characters()
      return characters


def search(parameter: str, value: str, list):
  for element in list:
    elem = element[f"{parameter}"]
    if value in elem or value == elem:
      return element


def get_characters():
    endpoint = f"/v1/public/characters"
      
    response = connect(endpoint, params)
    response = response.json()
    characters = response["data"]["results"]
    return characters

def get_character(name: str = None):
    endpoint = f"/v1/public/characters"
    
    response = connect(endpoint, params)
    response = response.json()
    characters = response["data"]["results"]

    if name:
      name = name.capitalize()

    character_or_empty = search("name", name, characters)

    if character_or_empty:
      return {
        "id": character_or_empty["id"],
        "name": character_or_empty["name"],
        "image": f"{character_or_empty['thumbnail']['path']}/standard_small.{character_or_empty['thumbnail']['extension']}",
        "appearances": f"{character_or_empty['comics']['available']}",
      }

def get_comic(title: str = None):
    endpoint = f"/v1/public/comics"

    response = connect(endpoint, params)
    response = response.json()
    comics = response["data"]["results"]
    
    if title:
      title = title.capitalize()
    
    comic_or_empty = search("title", title.capitalize(), comics)
    
    if comic_or_empty:
      return {
        "id": comic_or_empty["id"],
        "title": comic_or_empty["title"],
        "image": f"{comic_or_empty['thumbnail']['path']}/standard_small.{comic_or_empty['thumbnail']['extension']}",
        "onsaleDate": f"{comic_or_empty['dates'][0]['date']}",
      }
    return {}