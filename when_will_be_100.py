# python3
# takes name and age and tells when will you get 100th year
import time
name = input("Enter your name: ")
century = 100

try:
    age = int(input("Enter your age: "))
    if type(age) == 'int':
        print("enter your age in numbers")
    elif(age > 100):
        print("you are already crossed 100 or u r a liar !!")
    elif(age == 100):
        print("wow r u 100 !!")
    else:
        curr_year = int(time.strftime("%Y"))
        rem_years = century - age
        when_to_century = curr_year + rem_years
        print("%s will be 100 by the year %s and " % (name, when_to_century) +
              "he have left %s years" % (rem_years))
except ValueError:
    print("OOPS...! \nEnter age in numbers.")
