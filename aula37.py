"""
Repetições
While(enquanto)
Executa uma ação enquanto uma condição ser verdadeira
Break e Continue funcionam no while mais proximo
"""
# contador = 0

# while contador < 11:
#    print(contador)
#    contador += 1

#    if contador == 6:
#       continue
   


contador = int(input('Digite o Número Inicial: '))
limite_contador = int(input('Digite o limite do Contador: '))
numero__de_passos_para_pular = int(input('Digite de quanto em quanto vai pular: '))

while contador <= limite_contador:
    contador += numero__de_passos_para_pular
    
    if contador == 6:
        print('to no 6')
        continue
    
    if contador >= 7 and contador <= 10:
        print('Não vou mostrar o ', contador)
        continue
    
    print(contador)
