# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance()


txt1 = input("Digite uma frase ou palavra: ")
if isinstance(txt1, str):
    formatado = txt1.replace(" ","").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
else:
    print("Entrada inválida, digite uma frase ou palavra")