from faker import Faker
import random
import requests
import json

fake = Faker('pt_BR')

def generate_persona():
    persona = {
        'id': random.randint(10, 100),
        'username': fake.user_name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'address': fake.address(),
        'cpf': fake.cpf(),
        'password': fake.password(length=10, special_chars=False, upper_case=True, lower_case=True, digits=True)
    }
    return persona

persona = generate_persona()

url = 'http://desafiopython.jogajuntoinstituto.org/api/users/'

response = requests.post(url, json=persona)

print(f'Status Code: {response.status_code}')
print(f'Response: {response.json()}')


print(persona)

print(f'Password: {persona["password"]}')



# URL de login
login_url = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'

# Dados de login
login_data = {
    'email': persona["email"],
    'password': persona["password"]
}
login_response = requests.post(login_url, json=login_data)

if login_response.status_code == 200:
    print("    ")
    print('Login bem-sucedido!')
    print("    ")
    print(f'Login Response: {login_response.json()}')
    response_json = login_response.json()
    
    nome_arquivo = 'token_de_usuario'
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(response_json, arquivo, indent=4)
else:
    print('A senha ou o email está incorreto, tente novamente.')