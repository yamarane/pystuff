# python3
# Finding user input is odd or even
num = int(input("enter a num: "))
print(num)
if num % 2 == 0 and num % 4 == 0:
    print("your num divided by 2 n 4")
elif num % 2 == 0:
    print("you entered even number")
else:
    print("your num is odd")
