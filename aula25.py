nome = 'luiz'
preco = 1000
# O () só é necessário, caso tenha dois valores, por exemplo: %s e %f
# d e I para inteiro
# s para String
# f float
variavel = '%s, o preço total  R$%.2f' % (nome, preco)
print(variavel)