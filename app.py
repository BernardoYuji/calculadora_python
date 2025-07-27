#calculadora
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operador = (input('Digite o operador: '))

match operador:
    case '+':
        res = num1 + num2
    case '-':
        res = num1 - num2
    case '*':
        res = num1 * num2
    case '/':
        if num2 == 0:
            res = 'Divisão por zero'
        else:
            res = num1 / num2

print(f'O resultado é {res}')
