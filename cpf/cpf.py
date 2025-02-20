from cpf.gerar import GeradorCpf
from cpf.validar import ValidarCpf

class CpfValido:
    def __init__(self):
        self.gerar = GeradorCpf()
        self.cpf = self.gerar.gerar_cpf()

    def obter_numero(self):
        return self.cpf

    def obter_regiao(self):
        return ValidarCpf(self.cpf).regiao()

    def obter_cpf(self):
        return {
            'numero':self.obter_numero(),
            'regiao':self.obter_regiao()
        }