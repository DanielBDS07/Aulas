import requests

class MeuErro(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

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

try:
    login_response = requests.post(login_url, json=login_data)

except MeuErro as e:
    print('Ocorreu um erro, confira se as informações estão corretas') 


print(f'Login Status Code: {login_response.status_code}')
print(f'Login Response: {login_response.json()}')
