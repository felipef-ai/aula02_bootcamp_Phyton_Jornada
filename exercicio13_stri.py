# 13 Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida,
# imprima esta frase sem espaços em branco no início e no final.
#.strip() (remove espaços em branco no início e no final)

frase = input("Insira uma frase do seu gosto: ")
frase_junto = frase.strip()
print(f"A sua frase sem espaços no início e no fim, fica assim: {frase_junto}")
