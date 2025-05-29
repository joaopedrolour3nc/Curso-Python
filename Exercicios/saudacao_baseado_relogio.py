"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a Hora que for: ')


if hora == '0' or hora <= '11':
    print('Bom dia')
elif hora == "12" or hora <= "17":
    print('Boa tarde')
elif hora >= '18' or hora <= '23':
    print('Boa noite')
else:
    print('Hora inválida, digite um número entre 0 e 23')