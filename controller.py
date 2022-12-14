import parser
import view
import model

def check_enter():
    enter = view.input_enter()
    if enter.isdigit():
        model.set_first(enter)
    else:
        parser.set_expression(enter)

    #     for item in enter:
    #     if item.isdigit() and '+' or '-' or '*' or '/' in enter:
    #         model.set_expression(enter)
    # else:
    #     print('Ошибочка вышла!')

    # СДЕЛАТЬ ПРОВЕРКУ НА ДУРАКА!

def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.division_by_zero()
        else:
            model.set_second(number)
            break

def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def solution():
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
                print(f'Очень хорошо! Результат кнопочного калькулятора = {model.get_result()}')
                break
            input_second()
            solution()
    else:
        parser.pars_expression()
        print(f'Очень хорошо! Результат строкового калькулятора = {parser.get_result()}')




