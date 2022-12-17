
def input_enter():
    enter = input('Введите целое число или выражение: ') # принимает на вход число или выражение
    return enter

def input_number(): # вводим второе число для кнопочного калькулятора
    while True:
        try:
            number = int(input('Введите число: '))
            return number
        except:
            print('Ошибочка вышла!')

def input_operation(): # вводим оператор
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректную операцию!')

def print_to_console(value_text): # печатаем в консоль
    print(value_text)

def log_off(result): # выводим результат в консоль
    print(f'Очень хорошо! Ваш результат = {result}')

def check_equation(): # выводим ошибку (проверка на дурака)
    print('Введены некорректные данные, попробуйте ещё раз')

def division_by_zero(): # выводим ошибку деления на 0
    print('На ноль делить нельзя попробуйте ещё раз')