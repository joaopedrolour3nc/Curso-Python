"""
Introdução ao Try/except
try -> tentar executar um código
except -> ocorreu um erro ao tentar execultar
"""

numero_str = input('Vou dobrar o numero que você digitar: ')

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_str} é {numero_float *2:.2f}') 
except:
    print('Isso não é um numero')
# print(numero_str.isdigit())

