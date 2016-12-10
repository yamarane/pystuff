# python3
# this is example of list comprehensions
# for (set of values to iterate):
#   if (conditional filtering):
#       output_expression()
#           TO
# [output_expression() for(set of values to iterate) if(conditional filtering)]
import random
list = random.sample(range(100), 10)
# it generates random list with length 10
even_num_list = [i for i in list if i % 2 == 0]
# prints all even numbers in list
print(even_num_list)
