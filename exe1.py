comida = ( 'sushi' , 'macarrão' , 'atum' , 'lula' , 'batata')
lista = list(comida)
print(lista)

lista.append('torta')
lista.append('peixe')
print(lista)

lista.pop(6)
lista.pop(0)
print(lista)

print(lista[0])

tamanho_lista = len(lista)

print(tamanho_lista)

nome = str(input ("qual é o seu nome?: "))
idade =  float(input("qual é a sua idade?: "))
profissao = str(input ("qual é a sua Profissão?: "))

Pessoa = {'nome': nome, 'idade': idade, 'Profissão': profissao}

print('O teu nome é: ' , Pessoa['nome'])