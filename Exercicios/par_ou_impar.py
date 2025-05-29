"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')


try:
    numero_int = int(numero)
    numero_par_ou_impar = numero_int % 2 == 0
    if numero_par_ou_impar:
        print('Seu numero é Par')
    else:
        print('Seu numero é impar')
except:
    print('Você não digitou um numero Inteiro')