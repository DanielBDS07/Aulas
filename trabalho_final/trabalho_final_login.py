import requests
import json
from faker import Faker
import pandas as pd

print('   ')
print('Seja bem vindo Instituto Joga Junto')
print('   ')
email = input('Por favor, insira o seu email: ')
print('   ')
password = input('Agora insira sua senha: ')

# URL de login
login_url = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'

# Dados de login
login_data = {
    'email': email,
    'password': password
}


# ribeiroana-cecilia@example.com
# wo3vFNu24H

# Faz a requisição POST para fazer login
login_response = requests.post(login_url, json=login_data)

# Verifica o status code da resposta
if login_response.status_code == 200:
    print("    ")
    print('Login bem-sucedido!')
    print("    ")
    print(f'Login Response: {login_response.json()}')
    response_json = login_response.json()
    
    # Salvar o JSON em um arquivo
    nome_arquivo = 'token_de_usuario'
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(response_json, arquivo, indent=4)
else:
    print('A senha ou o email está incorreto, tente novamente.')
