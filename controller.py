import parser
import view
import model

def check_enter(): # проверяем, ввели число или выражение. Если введи число -> идем по алгоритму кнопочного калькулятора, если строку –> идём првоерять строку
    while True:
        enter = view.input_enter()
        if enter.isdigit():
            model.set_first(enter)
            break
        elif '/ 0' in enter:  # тут сразу сделала проверку деления на 0 в выражении
            view.division_by_zero()
        else:
            parser.set_expression(enter)
            break

def check_expression(): # (!) вот тут вопрос: проверка на ввод некорректных данных не срабатывает, почему?
    equation = parser.get_expression()
    for item in equation:
        if item.isdigit() and '+' or '-' or '*' or '/' in equation:
            parser.set_expression(equation)
        else:
            return True


def input_second(): #приняли второе число для кнопочного, проверили деление на 0 и записали
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.division_by_zero()
        else:
            model.set_second(number)
            break

def input_operation(): # приняли и записали операцию
    oper = view.input_operation()
    model.set_operation(oper)

def solution(): # приняли и посчитали операцию
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()
    else:
        return

    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())


def start():
    check_enter()
    if model.get_first():
        while True:
            input_operation()
            if model.get_operation() == '=':
                view.log_off(model.get_result())
                break
            input_second()
            solution()
    else:
        if check_expression():
            view.check_equation()
        parser.pars_expression()
        view.log_off(*parser.get_result())






