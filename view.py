
def input_enter():
    enter = input('Введите целое число или выражение: ') # принимает на вход число или выражение
    return enter

def input_number():
    while True:
        try:
            number = int(input('Введите число: '))
            return number
        except:
            print('Ошибочка вышла!')

def input_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректную операцию!')

def print_to_console(value_text):
    print(value_text)

def log_off(result):
    print(f'Очень хорошо! Ваш результат = {result}')

def check_equation():
    print('Ошибочка вышла!')

def division_by_zero():
    print('На ноль делить нельзя!')