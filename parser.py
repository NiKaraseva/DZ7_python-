
expression = ''
result = 0


def get_expression():
    global expression
    return expression

def get_result():
    global result
    return result

def set_expression(equation): # записали выражение
    global expression
    expression = equation


def pars_expression(): # парсим и считаем выражение
    global expression
    global result
    string = expression
    result = string.split()
    for i in range(len(result)):
        if result[i].isdigit():
            result[i] = int(result[i])
    while len(result) != 1:
        i = 0
        while ('*' in result or '/' in result) and i < len(result):
            if result[i] == '*':
                result[i - 1] = result[i - 1] * result[i + 1]
                if result[i - 1] == int(result[i - 1]):
                    result[i - 1] = int(result[i - 1])
                result.pop(i)
                result.pop(i)

            elif result[i] == '/':
                result[i - 1] = result[i - 1] / result[i + 1]
                result.pop(i)
                result.pop(i)
                if result[i - 1] == int(result[i - 1]):
                    result[i - 1] = int(result[i - 1])

            else:
                i += 1

        while ('+' in result or '-' in result) and i < len(result):
            if result[i] == '+':
                result[i - 1] = result[i-1] + result[i+1]
                result.pop(i)
                result.pop(i)
                i -= 1
            elif result[i] == '-':
                result[i - 1] = result[i-1] - result[i+1]
                result.pop(i)
                result.pop(i)
            else:
                i += 1
    return result
