vogais = {'a', 'e', 'i', 'o', 'u'}
contador = 0
for letra in palavra:
        
    letra_minuscula = letra.lower()
    if letra_minuscula in vogais:
        contador += 1
    
palavra = input("Digite uma palavra: ")
numero_vogais = contar_vogais(palavra)
print(f"A palavra '{palavra}' possui {numero_vogais} vogais.")


