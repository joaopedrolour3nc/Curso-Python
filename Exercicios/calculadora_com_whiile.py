""" Calculadora com While"""

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o Operador: ')
    tipo_de_numero = input('Você vai fazer um calculo com float ou Int: ')
    numeros_validos = None

    numero1_int = 0
    numero2_int = 0
    
    numero1_float = 0
    numero2_float = 0

    if tipo_de_numero == 'float':
        try:
            numero1_float = float(numero1)
            numero2_float = float(numero2)
            numeros_validos = True
        except:
            numeros_validos = None

        if numeros_validos is None:
            print('Um dos numeros são invalidos')
            continue
    else:
        try:
            numero1_int = int(numero1)
            numero2_int = int(numero2)
            numeros_validos = True
        except:
            numeros_validos = None

        if numeros_validos is None:
            print('Um dos numeros são invalidos')
            continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador Invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um Operadpr')
        continue
    print('Relizando a sua conta, veja o resultado abaixo....')
    
    if tipo_de_numero == 'float':

        if operador == '+':
            print(f'{numero1_float}+{numero2_float}=', numero1_float + numero2_float)

        elif operador == '-':
            print(f'{numero1_float}+{numero2_float}=', numero1_float - numero2_float)

        elif operador == '/':
            print(f'{numero1_float}+{numero2_float}=', numero1_float / numero2_float)
        
        elif operador == '*':
            print(f'{numero1_float}+{numero2_float}=', numero1_float * numero2_float)
        
        else:
            ...
    else:
        if operador == '+':
            print(f'{numero1_int}+{numero2_int}=', numero1_int + numero2_int)

        elif operador == '-':
            print(f'{numero1_int}+{numero2_int}=', numero1_int - numero2_int)

        elif operador == '/':
            print(f'{numero1_int}+{numero2_int}=', numero1_int / numero2_int)
        
        elif operador == '*':
            print(f'{numero1_int}+{numero2_int}=', numero1_int * numero2_int)

        sair = input('Você deseja sair? [S]').lower().startswith('s')

        if sair is True:
            break
