# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, 
# em seguida, imprima o dia, o mês e o ano separadamente.
#.split(sep) (divide a string em uma lista, utilizando sep como delimitador)

data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data_usuario.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)