import requests

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

# Faz a requisição POST para fazer login
login_response = requests.post(login_url, json=login_data)

# Verifica o status code da resposta
if login_response.status_code == 200:
    print('Login bem-sucedido!')
    print(f'Login Response: {login_response.json()}')
else:
    print('A senha ou o email está incorreto, tente novamente.')
