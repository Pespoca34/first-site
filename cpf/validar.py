class ValidarCpf:
    def __init__(self, cpf: str):
        self.cpf = self.remove_extra(cpf)
        self.numeros = [int(digito) for digito in self.cpf]

    @staticmethod
    def remove_extra(cpf: str) -> str:
        return cpf.replace('.', '').replace('-', '')

    def calcular_digito1(self) -> bool:
        soma = sum(self.numeros[i] * (10 - i) for i in range(9))
        resto = soma % 11
        return (0 if resto < 2 else 11 - resto) == self.numeros[9]

    def calcular_digito2(self) -> bool:
        soma = sum(self.numeros[i] * (11 - i) for i in range(10))
        resto = soma % 11
        return (0 if resto < 2 else 11 - resto) == self.numeros[10]

    def regiao(self):
        match self.numeros[8]:
            case 0 | 9: return 'Rio Grande do Sul'
            case 1: return 'Centro-Oeste'
            case 2: return 'Norte'
            case 3 | 4 | 5: return 'Nordeste'
            case 6 | 7 | 8: return 'Sudeste'

    def validar_cpf(self):
        if self.calcular_digito1() and self.calcular_digito2():
            return {
                'numero': f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}",
                'regiao': self.regiao()
            }
        return None  