first_number = 0
second_number = 0
operation = ''
result = 0

def get_first():
    global first_number
    return first_number

def get_second():
    global second_number
    return second_number

def get_operation():
    global operation
    return operation

def get_result():
    global result
    return result

def set_first(value): # записали первое число
    global first_number
    first_number = value

def set_second(value): # записали втрое число
    global second_number
    second_number = value

def set_operation(oper): # записали оператор
    global operation
    operation = oper

def addition(): # функция сложения
    global first_number
    global second_number
    global result
    result = int(first_number) + second_number

def difference(): # функция вычитания
    global first_number
    global second_number
    global result
    result = int(first_number) - second_number

def multiplication(): # функция умножения
    global first_number
    global second_number
    global result
    result = int(first_number) * second_number
    if result == int(result):
        result = int(result)

def division(): # функция деления
    global first_number
    global second_number
    global result
    result = int(first_number) / second_number
    if result == int(result):
        result = int(result)

