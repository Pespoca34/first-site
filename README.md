# First Site

Este é um projeto baseado em Flask que oferece funcionalidades relacionadas a cartões, CEPs, CPFs, e-mails e informações meteorológicas.

## 🚀 Tecnologias Utilizadas

- Flask
- Asyncio
- Random
- Datetime
- Requests

## 📂 Estrutura do Projeto

```
first-site/
│-- cartao/       # Funcionalidades relacionadas a cartões
│-- cep/          # Funcionalidades relacionadas a CEPs
│-- cpf/          # Funcionalidades relacionadas a CPFs
│-- email/        # Funcionalidades relacionadas a e-mails
│-- templates/    # Arquivos HTML para renderização
│-- weather/      # Funcionalidades relacionadas ao clima
│-- app.py        # Arquivo principal da aplicação Flask
│-- routes.py     # Definição das rotas
│-- gerar_ceps.py # Script para geração de CEPs
│-- requirements.txt # Dependências do projeto
│-- .gitignore    # Arquivo para ignorar arquivos desnecessários no repositório
│-- LICENSE       # Licença do projeto
```

## 📌 Como Executar o Projeto

1. Clone o repositório:
   ```sh
   git clone https://github.com/Pespoca34/first-site.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd first-site
   ```
3. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Execute a aplicação:
   ```sh
   python app.py
   ```
6. Acesse a aplicação em seu navegador:
   ```
   http://127.0.0.1:5000/
   ```

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo!

---

Feito por [Pespoca34](https://github.com/Pespoca34) 🚀
