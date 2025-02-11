# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = Pi vezes o Raio elevado ao quadrado;
# utilizei o math do Pi, importando direto da biblioteca python

import math
raio = float(input("Digite o raio: "))
area = math.pi * raio ** 2
print(f"A área do circulo é: {area}")