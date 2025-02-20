from random import randint

class GerarCartao:
    def __init__(self):
        self.numero = self.gerar_numeros()
        self.validade = self.gerar_validade()
        self.cvv = self.gerar_cvv()
    
    def gerar_numeros(self):
        numeros_4 = str(randint(1000, 9999))
        numeros_8 = str(randint(1000, 9999))
        numeros_12 = str(randint(1000, 9999))
        numeros_16 = str(randint(1000, 9999))

        cartao = f"{numeros_4} {numeros_8} {numeros_12} {numeros_16}"

        return cartao

    def gerar_validade(self):
        mes = str(randint(1, 12))
        ano = str(randint(25, 30))
        validade = f"{mes}/{ano}"

        return validade

    def gerar_cvv(self):
        cvv = str(randint(100, 999))

        return cvv

    def gerar_cartao(self):
        return {
            'numero': self.gerar_numeros(),
            'validade': self.gerar_validade(),
            'cvv': self.gerar_cvv()
        }