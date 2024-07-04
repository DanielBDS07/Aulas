
import requests

def verificar_login(email, senha):
    url = 'http://desafiopython.jogajuntoinstituto.org/api/users/login/'
    dados = {
        'email': email,
        'senha': senha
    }

gmail = input('Digite o seu email: ')
senha = input('Digite sua senha: ')

response = requests.get("http://desafiopython.jogajuntoinstituto.org/api/users/login/")

if senha and gmail == response:
    print('Seu login foi bem sucedido')
else:
    print('O seu email ou senha esta incorreto')
