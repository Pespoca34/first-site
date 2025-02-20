import asyncio
from cep.gerar import GeradorCep
from cep.cep import CepValido
from database import criar_tabela, inserir_cep

async def main(qtd=50):
    criar_tabela()
    gerador = GeradorCep()
    validador = CepValido()

    task = [validador.validar_cep(gerador.gerar_cep()) for _ in range(qtd)]
    resultado = await asyncio.gather(*task)

    for dados in resultado:
        if dados and 'cep' in dados:
            inserir_cep(
                dados['cep'],
                dados.get('logradouro', ''),
                dados.get('bairro', ''),
                dados.get('cidade', ''),
                dados.get('estado', '')
            )
    print(f"{qtd} ceps gerados e validados com sucesso")

if __name__ == '__main__':
    asyncio.run(main())