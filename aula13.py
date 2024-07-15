nome = 'João'
peso = 55
altura = 1.83

imc = peso / (altura * altura)

# :.(um numero para saber quantas casa decimais)f formarta a quantidade que vai aparecer
# Após o .
linha_1 = f'{nome} tem {altura:.2f} de altura' 
linha_2 = f'pesa {peso} Kilos e o seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3 )