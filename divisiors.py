# python3
# Create a program that asks the user for a number and
# then prints out a list of all the divisors of that number and will tell you is it prime or not !
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
user_input = int(input("enter a number: "))
list1 = []
for i in range(1, user_input+1):
    if (user_input % i) == 0:
        list1.append(i)
print("%s is divisible by %s " % (user_input, list1))
# Is user_input prime or not
if len(list1) == 2:
    print("%s is prime" % user_input)
else:
    print("%s is not prime" % user_input)
