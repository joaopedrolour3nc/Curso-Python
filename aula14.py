# Out of Range é que eu to buscando a mais do que eu tenho
# a={Aqui é o Indice que vou querer mostrar, mas preciso lembrar que começa no 0}
# nome3=c é um parâmetro nomeado


a = 'AAAAAAA'
b = 'B'
c = 1.144884

string ='a={0} a={0} a={0} a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)

print(formato)