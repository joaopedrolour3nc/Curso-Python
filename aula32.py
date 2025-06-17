"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')


if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input("Digite a Hora que é agora: ")

if horario >= '0' and horario <= '11':
    print("Bom dia")
elif horario >= '12' and horario <= '17':
    print('Boa Tarde')
else:
    print('Boa Noite') 
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_do_usuario = input("Digite seu primeiro nome: ")
tamanho_do_nome = len(nome_do_usuario)

if tamanho_do_nome <= 4:
    print('Seu nome é curto')
elif tamanho_do_nome >= 5 and tamanho_do_nome <= 6:
    print("Seu nome é normal")
else:
    print('Seu nome é muito grande')