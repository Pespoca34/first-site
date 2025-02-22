import requests

def obter_email(email):
    url = f'https://leakcheck.io/api/public?check={email}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}