from cartao.gerar import GerarCartao
from cartao.validar import ValidarCartao

class CartaoValido:
    def __init__(self):
        self.gerar = GerarCartao()  
        self.cartao = None
        self.gerar_e_validar()
    
    def gerar_e_validar(self):
        while True:
            dados_cartao = self.gerar.gerar_cartao()  
            
            validar = ValidarCartao(**dados_cartao)
            if validar.validar_cartao():
                self.cartao = dados_cartao
                break

    def obter_cartao(self):
        return self.cartao