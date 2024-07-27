"""
Operadores in e not in
Strings são iteraveis 

"""
"""
Iteravel é um  negócio que você pode navegar item por item

Começa do zero
 0  1  2  3  4  5
 o  t  a  v  i  o
-6 -5 -4 -3 -2 -1
"""
# nome = 'otavio'
# print(nome[2])

# print('a' in nome)
# print('z' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('z' not in nome)

nome = input("Digite seu nome: ")

encontrar = input("Digite o que você quer encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')