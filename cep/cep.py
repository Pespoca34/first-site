import sqlite3
import random
from dotenv import load_dotenv
import os

load_dotenv()

def obter_dados():
    path = os.getenv('CEP_DB_PATH')
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('SELECT cep, estado, logradouro, bairro FROM ceps')
    rows = cursor.fetchall()

    if rows:
        random_row = random.choice(rows)
        dados = {
            'cep': random_row[0],
            'estado': random_row[1],
            'logradouro': random_row[2],
            'bairro': random_row[3]
        }
    else:
        dados = {}

    conn.close()
    return dados