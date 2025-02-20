from random import randint

class GeradorCpf:
    def __init__(self):
        self.cpf = None

    def gerar_numeros(self):
        self.cpf = [randint(0, 9) for _ in range(9)]
        return self.cpf

    def calcular_digito1(self, cpf):
        soma = sum(cpf[i] * (10 - i) for i in range(9))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    def calcular_digito2(self, cpf):
        soma = sum(cpf[i] * (11 - i) for i in range(10))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    def gerar_cpf(self):
        cpf = self.gerar_numeros()
        cpf.append(self.calcular_digito1(cpf))
        cpf.append(self.calcular_digito2(cpf))

        cpf_str = ''.join(map(str, cpf))  
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"