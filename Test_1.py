operand_grant = False
operand_1_grant = False

operand = input('Введіть перше число: ')
while operand_grant == False:
    try:
        operand = int(operand)
        operand_grant = True
    except:
        print('Введене некоректне число, повторіть введення')
        operand = input('Введіть перше число: ')

list_operator = ('+', '-', '/', '*')
operator_grant = False
while operator_grant == False:
    operator = input('Введіть дію (+, -, *, /)')
    count = 0
    for i in list_operator:
        if operator == i:
            operator_grant = True
        else:
            if count == 0:
                print('Введена некоректна дія, повторіть введення.')
                count += 1

operand_1 = input('Введіть друге число: ')
while operand_1_grant == False:

    try:
        operand_1 = int(operand_1)
        operand_1_grant = True
    except:
        print('Введене некоректне число, повторіть введення')
        operand_1 = input('Введіть друге число: ')


if operator == '+':
    result = operand + operand_1
    r = 'суммування'
    print(f'Результат  {r}  = ', result)
elif operator == '-':
    result = operand - operand_1
    r = 'віднімання'
    print(f'Результат  {r}  = ', result)
elif operator == '*':
    result = operand * operand_1
    r = 'множення'
    print(f'Результат  {r}  = ', result)
elif operator == '/':
    result = operand / operand_1
    r = 'ділення'
    print(f'Результат  {r}  = ', result)
