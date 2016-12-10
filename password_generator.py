# Python 3
# help(string)
# ****************************  Its string module  ****************************
# DATA
#     ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     digits = '0123456789'
#     hexdigits = '0123456789abcdefABCDEF'
#     octdigits = '01234567'
#     printable = '0123456789abcdefghijklmnopqrstuvwxyz
#                    ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     whitespace = ' \t\n\r\x0b\x0c'
import string
import random
password = input("Please enter weak, medium or strong to choose password :")


def weak_password():
    print("here is your weak password !\nIt doesn't have capitol letter and symbol and length is 8")
    return random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.digits)


def medium_password():
    print("Here is your medium password !\nIt has capitol letter, digit and length is 8")
    return random.choice(string.ascii_uppercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.digits)


def strong_password():
    print("Here is your strong password !\nIt has capitol letter, digit, symbol and length is 10")
    return random.choice(string.ascii_uppercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.ascii_lowercase)\
        + random.choice(string.digits)\
        + random.choice(string.punctuation)


def main():
    if password == 'weak':
        print(weak_password())
    elif password == 'medium':
        print(medium_password())
    elif password == 'strong':
        print(strong_password())
    else:
        print("You need to select one of these types \'weak, medium or strong\'")


if __name__ == '__main__':
    main()
