dolar = 5.45

produto = int(input('Digite quanto custa o valor do Produto em Dòlar: '))
valor_em_real = (produto * dolar)
print(valor_em_real)
imposto = int(input("Qual vai ser a porcentagem do  imposto cobrado?"))
valor_do_imposto = (valor_em_real * imposto) / 100
print(valor_do_imposto)
valor_do_produto = valor_do_imposto + valor_em_real
print("O valor do produto em real é ",valor_em_real) 
print("O Valor do imposto cobrado é", valor_do_imposto) 
print("O valor final do produto vai ser ", valor_do_produto)