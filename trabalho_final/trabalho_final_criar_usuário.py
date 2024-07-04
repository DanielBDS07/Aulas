from faker import Faker
import random
import requests

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

# Print the entire persona
print(persona)

# Print only the password of the persona
print(f'Password: {persona["password"]}')