from faker import Faker
import random

faker = Faker('pt_BR')

persona = {
    'nome': faker.name(),
    'cidade': faker.address(),
    'idade': faker.random_int(min=8, max=9)
}

print(persona)

