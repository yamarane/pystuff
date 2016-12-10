# python3
# this program takes list, symbol(*,/,+,-,**) and a num then gives result as list.
user_list = list(input("Enter list of values: "))
symbol = input("Enter a symbol caliculation: ")
number = int(input("Enter a num to find in list: "))


def multipy(user_list, num):
    multipy_list = [int(val) * num for val in user_list]
    return(multipy_list)


def divide(user_list, num):
    divided_list = [int(val)/num for val in user_list]
    return divided_list


def add(user_list, num):
    add_list = [int(val) + num for val in user_list]
    return add_list


def minus(user_list, num):
    minus_list = [int(val) - num for val in user_list]
    return minus_list


def mod(user_list, num):
    mod_list = [int(val) % num for val in user_list]
    return mod_list


def power(user_list, num):
    pow_list = [int(val) ** num for val in user_list]
    return pow_list
# Python don't have switch case so i used dictionary to fulfill that.
symbols = {
    '*': multipy,
    '/': divide,
    '+': add,
    '-': minus,
    '%': mod,
    '**': power
}

if __name__ == "__main__":
    print(symbols[symbol](user_list, number))
