result = 0
operand = None
operator = None
wait_for_number = True
operators = ('+', '-', '*', '/', '=')
data_input = ''
rezult_list = list()
index_count = 0


# Перевірка чи операнд це число
def check_operand(data_input):

    try:
        data_input = int(data_input)
        return True
    except:
        return False

# Зміна тексту вводу операнда, якщо він не перший. Та перевірка на коректність
def text_operand():
    if len(rezult_list) == 0:
        data_input = input('Введіть перше число: ')
        check_operand(data_input)
        if check_operand(data_input) == True:
            rezult_list.append(int(data_input))
            text_operator()
        else:
            print('Помилка у введенні числа')
            text_operand()
    else:
        data_input = input('Введіть чергове число: ')
        check_operand(data_input)
        if check_operand(data_input) == True:
            rezult_list.append(int(data_input))
            text_operator()
        else:
            print('Помилка у введенні числа, повторіть введення.')
            text_operand()


# Перевірка чи це знак оператора
def check_operators(data_input):
    if data_input in operators:
        return True
    else:
        return False

# Зміна тексту вводу оператора, якщо він не перший. та перевірка на коректність.
def text_operator():
    
    if len(rezult_list) == 1:
        data_input = input('Введіть знак операції (+, -, /, *): ')
        
        if check_operators(data_input) == True:
            rezult_list.append(data_input)
            text_operand()
        else:
            print('Помилка у введенні оператора, повторіть введення.')
            text_operator()
    else:
        
        data_input = input('Введіть знак операції (+, -, /, *) або знак "=" для початку процесу: ')            
        if check_operators(data_input) == True and data_input != '=':
            rezult_list.append(data_input)
            text_operand()                           
        else:
            if data_input == '=':
                print('Виконую розрахунок.')
            else:
                print('Помилка у введенні оператора, повторіть введення.')
                text_operator()



            

            



# Основна процедура

    
text_operand()  

for i in rezult_list:
    try:
        i = int(i)
        if index_count == 0:
            result += i
            index_count += 1
        else:
            if znak == '+':
                result = result + i
            elif znak == '-':
                result = result - i
            elif znak == '/':
                result = result / i
            elif znak == '*':
                result = result * i
            index_count += 1
    except:
        znak = i
        index_count += 1
print('Результат: ', result)
    

