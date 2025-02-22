import requests
from dotenv import load_dotenv
import os

load_dotenv()

def check_email(email):
    url = "https://email-leak-search.p.rapidapi.com/api/search"

    querystring = {"email":email}

    headers = {
    	"x-rapidapi-key": os.getenv('RAPID_API'),
    	"x-rapidapi-host": os.getenv('RAPID_HOST')
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
