"""
Operador Lógico OR
Quando um for verdadeiro ele valida tudo como verdadeiro 

"""

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
#     print("Seja Bem vindo")
# else:
#     print("Sair")

# Avaliação de Curto Circuito 



senha = (0 or False or 0 or 'ABC')
print("A senha é:",senha)