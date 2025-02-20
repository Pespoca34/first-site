from random import choice,randint

class GeradorCep:
    def __init__(self):
        self.cep = None
        self.faixas_cep = None
        self.estado = None
        self.parametros()

    def parametros(self):
        self.faixas_cep = {
            "AC": ("69900000", "69999999"),
            "AL": ("57000000", "57999999"),
            "AP": ("68900000", "68999999"),
            "AM": ("69000000", "69299999"), 
            "BA": ("40000000", "48999999"),
            "CE": ("60000000", "63999999"),
            "DF": ("70000000", "73699999"),
            "ES": ("29000000", "29999999"),
            "GO": ("72800000", "76799999"),
            "MA": ("65000000", "65999999"),
            "MT": ("78000000", "78899999"),
            "MS": ("79000000", "79999999"),
            "MG": ("30000000", "39999999"),
            "PA": ("66000000", "68899999"),
            "PB": ("58000000", "58999999"),
            "PR": ("80000000", "87999999"),
            "PE": ("50000000", "56999999"),
            "PI": ("64000000", "64999999"),
            "RJ": ("20000000", "28999999"),
            "RN": ("59000000", "59999999"),
            "RS": ("90000000", "99999999"),
            "RO": ("76800000", "76999999"),
            "RR": ("69300000", "69399999"),
            "SC": ("88000000", "89999999"),
            "SP": ("01000000", "19999999"),
            "SE": ("49000000", "49999999"),
            "TO": ("77000000", "77999999")
        }

    def gerar_cep(self):
        estados = list(self.faixas_cep.keys())
 
        #? Escolhe um estado aleatório
        estado_aleatorio = choice(estados)

        #*Pega a faixa de CEP desse estado escolhido
        faixa = self.faixas_cep[estado_aleatorio]
        
        cep = randint(int(faixa[0]), int(faixa[1]))

        self.cep = f"{cep:08d}"
        return self.cep

    def obter_cep(self):
        return str(self.cep)