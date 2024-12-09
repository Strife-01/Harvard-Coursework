#!/usr/bin/python


def main() :
    math = input('Exrpession: ')
    math_content = math.split()
    x = float(math_content[0])
    math_operand = math_content[1]
    y = float(math_content[2])

    if math_operand == '+' : print(x + y)
    elif math_operand == '-' : print(x - y)
    elif math_operand == '*' : print(x * y)
    elif math_operand == '/' : print(x / y)
    else : print('invalid operation')


main()
