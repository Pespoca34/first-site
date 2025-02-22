from cep.gerar import GeradorCep
from cep.request import Request
import asyncio

class CepValido:
    def __init__(self):
        self.url = 'https://viacep.com.br/ws/{}/json'
        self.gerador = GeradorCep()

    async def validar_cep(self, cep):
        url = self.url.format(cep)
        response = await asyncio.to_thread(Request(url).get)
        
        if 'erro' not in response:
            return response
        else:
            print(f'O CEP {cep} não é válido')

    async def obter_cep(self):
        while True:
            task = [self.validar_cep(self.gerador.gerar_cep()) for _ in range(20)]
            result = await asyncio.gather(*task)

            for cep in result:
                if cep:
                    return cep