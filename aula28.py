"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
# 0123
# joao
#-4321 

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if nome == "" or idade == "":
    print("Erro para iniciar o programa, faltou alguma informação.")
else:
    print("Seu nome é", nome)
    print("Seu nome invertido é",nome[::-1])
    print("Seu nome tem(ou não)espaços",' ' in nome)
    print('A quantidade de letras do seu nome é de ',len(nome))
    print('A primeira letra do seu nome é ',(nome[0:1:]))
    print('A Ultima letra do seu nome é ',(nome[3::]))
    