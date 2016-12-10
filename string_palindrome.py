# python3
# checks inout string is palindrome or not
user_input = input("enter a string: ")
if user_input == user_input[::-1]:
    print("%s is palindrome" % user_input)
else:
    print("%s is not palindrome" % user_input)
    print("A palindrome is a string that reads the same forwards and backwards.")
