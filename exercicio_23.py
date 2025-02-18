# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

try:

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    operador = input("Digite o operador: + , - , * , /")
    if operador == "+":
        resultado = (num1+num2)
    elif operador == "-":
        resultado = (num1-num2)
    elif operador == "*":
        resultado = (num1*num2)
    elif operador == "/" and num2 != 0:
        resultado = (num1/num2)
    else:
        print("Entrada inválida, você digitou ZERO!")
    print("O Resultado é: ", resultado)

except TypeError:
    print("Digite um número válido")
except NameError:
    print("O resultado não pode ser exibido, tente novamente!!!")
