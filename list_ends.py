# python3
# prints list with starting and ending values of input list
user_input_list = list(input("please enter list of values: "))
length = len(user_input_list)-1


def list_ends(user_input_list1, end_list):
    end_list.append(user_input_list1[0])
    end_list.append(user_input_list1[length])
    return end_list
print(list_ends(user_input_list, end_list=[]))
