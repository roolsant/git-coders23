valor1 = int(input('Digite um valor :'))
valor2 = int(input('Digite outro valor :'))
calculo = input('Digite a operação [ +, -, / ou *] :')


def calculadora(num1=valor1, num2=valor2, oeracao=calculo):
    if calculo == '+':
        return num1+num2
    elif calculo == '-':
        return num1-num2
    elif calculo == '/':
        return num1/num2
    elif calculo == '*':
        return num1*num2


resultado = calculadora(valor1, valor2, calculo)

print(resultado)
