

def verifica_cep_frete_gratis(cep):
    # Definindo as faixas de CEPs para as regiões Norte e Nordeste
    regioes_norte = [
        (69900, 69999),  # AC
        (57000, 57999)   # AL
        # Continuar com as demais faixas de CEPs para os estados da região Norte e Nordeste
    ]
    
    regioes_nordeste = [
        (40000, 48999),  # BA
        (64000, 64999)   # PI
        # Continuar com as demais faixas de CEPs para os estados da região Nordeste
    ]

try:
        cep_numero = int(input("Qual o seu cep?: "))
except ValueError:
    return False  # Se não conseguir converter, retorna False
    
    # Verificando se o CEP está dentro das faixas das regiões Norte ou Nordeste
for inicio, fim in regioes_norte:
    if inicio <= cep_numero <= fim:
        return True
    
for inicio, fim in regioes_nordeste:
    if inicio <= cep_numero <= fim:
        return True
    


cep_usuario = input("Digite seu CEP para verificar elegibilidade para frete grátis: ")
if verifica_cep_frete_gratis(cep_usuario):
    print("Você tem direito a frete grátis!")
else:
    print("Infelizmente o frete não é grátis para o seu CEP.")