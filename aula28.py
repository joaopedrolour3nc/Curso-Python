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

if nome == "" and idade == "":
    print("Erro para iniciar o programa, faltou alguma informação.")
else:
    print(f"Seu nome é", {nome})
    print(f"Seu nome invertido é",{nome[::-1]})
    if '' in nome:
        print(f'Seu nome tem espaço')
    else:
        print(f'Seu nome não tem espaço')
    print(f'A quantidade de letras do seu nome é de ',len(nome))
    print(f'A primeira letra do seu nome é {nome[0:1:]}')
    print(f'A Ultima letra do seu nome é {nome[-1]}')
    