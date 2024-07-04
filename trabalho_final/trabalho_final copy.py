import requests


# Credenciais fornecidas
print('   ')
print('Seja bem vindo Instituto Joga Junto')
print('   ')
email = (input('Por favor, insira o seu email: '))
print('   ')
password = (input('Agora insira sua senha: '))


# URL de login
login_url = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'

# Dados de login
login_data = {
    'email': email,
    'password': password
}

# Faz a requisição POST para fazer login
login_response = requests.post(login_url, json=login_data)

print(f'Login Status Code: {login_response.status_code}')
print(f'Login Response: {login_response.json()}')
