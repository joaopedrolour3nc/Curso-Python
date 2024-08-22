"""
Iterando Strings com While
"""

# #       012345678910
# nome = 'Luiz Otávio'
# #     1110987654321
# tamanho_do_nome = len(nome)
# print(nome)
# print(tamanho_do_nome)


# print(nome[3])

nome = 'Luiz Otávio'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)