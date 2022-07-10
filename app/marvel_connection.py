from dotenv import load_dotenv
import requests
import os

load_dotenv()
MARVEL_BASE_URL = os.environ["MARVEL_BASE_URL"]

def connect(endpoint: str, params: dict, request_type: str = "GET"):
  url = f"{MARVEL_BASE_URL}{endpoint}?{params}" if params else f"{MARVEL_BASE_URL}{endpoint}"
  response = requests.request(request_type, url)
  response.raise_for_status()
  return response