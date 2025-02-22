import asyncio
import sqlite3
from cep.cep import CepValido

class BancoDeDados:
    def __init__(self, nome="ceps.db"):
        self.conexao = sqlite3.connect(nome)
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao:
            self.conexao.execute(
                """CREATE TABLE IF NOT EXISTS ceps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cep TEXT UNIQUE,
                    logradouro TEXT,
                    bairro TEXT,
                    cidade TEXT,
                    estado TEXT
                )"""
            )

    def salvar_cep(self, dados):
        if dados:
            with self.conexao:
                self.conexao.execute(
                    "INSERT OR IGNORE INTO ceps (cep, logradouro, bairro, cidade, estado) VALUES (?, ?, ?, ?, ?)",
                    (dados["cep"], dados.get("logradouro", ""), dados.get("bairro", ""), dados.get("localidade", ""), dados.get("uf", ""))
                )

async def coletar_ceps():
    cep_validador = CepValido()
    banco = BancoDeDados()
    ceps_coletados = 0

    while ceps_coletados < 100:
        tarefas = [cep_validador.obter_cep() for _ in range(min(50, 100 - ceps_coletados))]
        resultados = await asyncio.gather(*tarefas)
        
        for resultado in resultados:
            if resultado:
                banco.salvar_cep(resultado)
                ceps_coletados += 1

if __name__ == "__main__":
    asyncio.run(coletar_ceps())
