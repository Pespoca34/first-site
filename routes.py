from app import app
from flask import render_template, request
from cartao.cartao import CartaoValido
from cpf.cpf import CpfValido
from cpf.validar import ValidarCpf
from weather.weather import get_weather
from cep.cep import CepValido


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cartao', methods=['GET','POST'])
def cartao():
    dados = None
    if request.method == 'POST':
        dados = CartaoValido().obter_cartao()
    return render_template('cartao.html', dados=dados)

@app.route('/cpf', methods=['GET','POST'])
def cpf():
    dados = None
    if request.method == 'POST':
        dados = CpfValido().obter_cpf()
    return  render_template('cpf.html', dados=dados)

@app.route('/cep', methods=['GET'])
def cep():
    return render_template('desenvolvimento.html')

@app.route('/validar',methods=['GET','POST'])
def validar():
    dados = None
    if request.method == 'POST':
        cpf_digitado = request.form.get('cpf')
        if len(cpf_digitado) != 11:
            dados = {
                'tam': True
            }
            return render_template('validar.html', dados=dados)


        validador = ValidarCpf(cpf_digitado)
        resultado = validador.validar_cpf()

        if resultado:
            dados = {
                'numero': resultado['numero'],
                'regiao': resultado['regiao'],
                'valid': True
            }
        else:
            dados = {
                'valid': False
            }

        return render_template('validar.html', dados=dados)

    return render_template('validar.html', dados=None)

@app.route('/weather', methods=['GET','POST'])
def weather():
    dados = None
    if request.method == 'POST':
        cidade = request.form.get('cidade')
        dados = get_weather(cidade)
        
    return render_template('weather.html', dados=dados)

@app.route('/email', methods=['GET','POST'])
def email_checker():
    return render_template('email.html')