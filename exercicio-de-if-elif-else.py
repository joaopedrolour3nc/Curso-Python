primeiro_valor = input("Digite o Primeiro Valor: ")
segundo_valor = input("Digite o Segundo Valor: ")

if primeiro_valor > segundo_valor:
    print("O valor ",primeiro_valor, "è maior que o Segundo Valor digitado que é ", segundo_valor)
elif primeiro_valor < segundo_valor:
    print("O Segundo valor ", segundo_valor, "É maior que o Primeiro ", primeiro_valor)
elif primeiro_valor == segundo_valor:
    print("Os números são iguais")
else:
    print("Reinicie o Código")
