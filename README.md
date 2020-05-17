# Flask-from-Scratch

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Sete os valores das variáveis de ambiente de conexão ao mailtrap
* Sete os valores do arquivo de conexão ao banco de dados Postgresql
* Rode o App.

```
git clone https://github.com/leandro-matos/Flask-from-Scratch.git
cd Flask-from-Scratch
python3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
flask run
```

Deploy no Heroku: https://acme-feedback.herokuapp.com/