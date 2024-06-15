n1 = int(input('Digite a Primeira nota: '))
n2 = int(input('Digite a Segunda nota: '))
n3 = int(input('Digite a Terceira  nota: '))

media = (n1 + n2 + n3) / 3
print(media)
if media > 6:
    print("Parabéns, você foi aprovado pois a sua nota é",media, "E ele é maior que 6")
elif media == 6:
    print("olha,quase em, sua media foi ", media, "E quase você não passou")
elif media >= 3 or media == 5:
    print("Você vai precisar fazer a recuperação, pois a sua media foi", media)
else:
    print("Infelizmente você foi reprovado.")

