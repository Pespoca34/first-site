import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city):
    api_key = os.getenv('WEATHER_API')

    if not api_key:
        return 'Erro: Chave da API não encontrada!'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt"

    try:
        response = requests.get(url)
        data = response.json()

        dicio = {}
        if response.status_code == 200:
            dicio['cidade'] = data['name']
            dicio['temperatura'] = data['main']['temp']
            dicio['descricao'] = data['weather'][0]['description']
            dicio['pais'] = data['sys']['country']
            return dicio
        else:
            return f"Erro na requisição: {data['message']}"

    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"
