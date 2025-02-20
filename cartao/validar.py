from datetime import datetime

class ValidarCartao:
    def __init__(self, numero:str, validade:str, cvv:str):
        self.numero = self.remove_spaces(numero)
        self.numero = self.transform_to_list(self.numero)
        self.validade = validade
        self.cvv = cvv

    @staticmethod
    def remove_spaces(numero:str):
        return numero.replace(' ', '')
    
    @staticmethod
    def transform_to_list(numero:str):
        numero = [int(digito) for digito in numero]
        return numero

    def verificar_bandeira(self):
        numero = self.numero
        match numero[0]:
            case 4:
                return 'Visa'
            case 5:
                if numero[1] in range(1, 6):
                    return 'Mastercard'
                elif numero[1] == 0:
                    return 'Maestro'
            case 3:
                if numero[1] in (4, 7):
                    return 'American Express'
                if numero[1] == 0:
                    return 'Diners Club'
            case 6:
                if numero[1] in (0, 5):
                    return 'Discover'
                if numero[1] == 2:
                    return 'Mir'
    
    def validar_numero(self) -> bool:
        numero = self.numero[::-1]
        soma = 0
        posicoes_impares = []
        for i in range(1, len(numero), 2):
            valor_dobrado = numero[i] * 2
            if valor_dobrado > 9:
                valor_dobrado -= 9
            posicoes_impares.append(valor_dobrado)
        soma += sum(posicoes_impares)

        for i in range(0, len(numero), 2):
            soma += numero[i]

        return soma % 10 == 0

    def validar_validade(self) -> bool:
        try:
            if "/" in self.validade:
                mes, ano = self.validade.split('/')
            else:
                return False

            mes = int(mes)
            ano = int(ano) 

            if ano < 100:
                ano += 2000

            today = datetime.today()
            ano_atual = today.year
            mes_atual = today.month

            return (1 <= mes <= 12) and (ano > ano_atual or (ano == ano_atual and mes >= mes_atual))
        except ValueError:
            return False

    def validar_cvv(self) -> bool:
        if not self.cvv.isdigit():
            return False

        bandeira = self.verificar_bandeira()
        tamanho_cvv = len(self.cvv)

        if bandeira in ['Visa', 'Mastercard', 'Maestro', 'Discover']:
            return tamanho_cvv == 3
        elif bandeira in ['American Express', 'Diners Club']:
            return tamanho_cvv == 4
        else:
            return False

    def validar_cartao(self) -> bool:
        return self.validar_numero() and self.validar_validade() and self.validar_cvv()