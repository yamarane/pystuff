# python3
# Take two lists and write a program that returns a list
# contains only the elements are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
import random
list1 = random.sample(range(30), 10)
list2 = random.sample(range(30), 5)
print(list1)
print(list2)
# Method: 1
match_list = []
for i in list2:
    if i in list1:
        match_list.append(i)

print(match_list)
# Method: 2 (achieve samething in one line)
super_list = [i for i in list1 if i in list2]
print(super_list)
