
# 计算符号
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1- n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# 创建字典
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculation():
    num1 = float(input('What is the first number?:'))


    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input('Pick an operation :')
        num2 = float(input('What is the next number?:'))
    # 自己的做法
    # if operation_symbol == '+':
    #     num_end=add(num1, num2)
    # elif operation_symbol == '-':
    #     num_end=subtract(num1, num2)
    # elif operation_symbol == '*':
    #     num_end=multiply(num1, num2)
    # elif operation_symbol == '/':
    #     num_end=divide(num1, num2)

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation:\n") == 'y':
            num1 = answer
        else:
            should_continue =False
            calculation()
calculation()

