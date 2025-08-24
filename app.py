#calculadora

# Receive two input from the user as numbers and one input as an operator
num1 = float(input('type the first number: '))
num2 = float(input('type the second number: '))
operator = (input('type the operator: '))

# Perform the operation based on the operator input
match operator:
    case '+':
        res = num1 + num2
    case '-':
        res = num1 - num2
    case '*':
        res = num1 * num2
    case '/':
        if num2 == 0:
            res = 'Division by zero'
        else:
            res = num1 / num2

# Print the result
print(f'The final result is: {res}')
