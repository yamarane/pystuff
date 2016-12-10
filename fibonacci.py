# python3
# This program gives desired no of fibonacci numbers
user_input = int(input("how many numbers you want in fibonacci series: "))
fib0, fib1 = 1, 1
fib = []
fib.append(fib0)
fib.append(fib1)
# now fib has [1,1]


def fibonacci(user_input):
    # i in range(0, 3)-->i i in [0,1,2]
    for i in range(0, user_input):
        # fib[0] + fib [0+1] ....fib [1] + fib [2].....fib[2] + fib [2+1]
        fib.append(fib[i]+fib[i+1])
    return fib
# [1,1,2,3,5]
print(fibonacci(user_input))
