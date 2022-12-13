import view
import model

def input_first():
    number = view.input_number()
    model.set_first(number)


def input_second():
    number = view.input_number()
    model.set_second(number)

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

def start():
    input_first()
    input_operation()
    input_second()
    solution()
