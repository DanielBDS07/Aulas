import pandas as pd
from faker import Faker
fake = Faker('pt_BR')


personas_list = []
def create_persona() -> dict:

    data = {
        "nome": fake.name(),
        "cidade": fake.city(),
        "idade": fake.random_int(18, 100)
        }
    return data

def gerar_personas_qtd(numeros_de_personas):
    for i in range(numeros_de_personas):
        personas_list.append(create_persona())





df_lista_de_personas = pd.DataFrame(lista_de_personas)
print(df_lista_de_personas)

df_lista_de_personas.to_csv('lista_de_pessoas_cvs', index=False)