import requests
from dotenv import load_dotenv
import os

load_dotenv()

def requested(email:str) -> dict:
    url = "https://email-leak-search.p.rapidapi.com/api/search"

    querystring = {"email": email}

    headers = {
    	"x-rapidapi-key": os.getenv('LEAKED_API'),
    	"x-rapidapi-host": os.getenv('LEAKED_HOST')
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Invalid email'}

def search(email:str) -> dict:
    return requested(email)
