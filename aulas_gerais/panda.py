import pandas as pd

dados = {
    "nome": ["joão" , "marta" , "ary" , "mateus", "Michelle", "Carlos"],
    "Idade": [51,37,23,24,33,12],
    "cidade": ["Recife","Recife","Recife","Salvador","São paulo","Manaus"]    
}
df = pd.DataFrame(data=dados)

moradores_recife = df[df['cidade'] == 'Recife']
print(moradores_recife)
