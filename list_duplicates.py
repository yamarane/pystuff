# python3
# this program takes list as input and returns new list without duplicates
user_list = list(input("enter list with some duplicates: "))


def remove_duplicates1(user_list):
    user_list.sort()
    i = len(user_list) - 1
    while i > 0:
        if user_list[i] == user_list[i - 1]:
            user_list.pop(i)
        i -= 1
    return user_list

# remove_duplicates2 copied from here https://gist.github.com/prgrm/12788827aa38748214df#file-ex13


def remove_duplicates2(user_list):
    new_list = []
    for i in user_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def remove_duplicates3(user_list):
    return sorted(list(set(user_list)))
print("method 1", remove_duplicates1(user_list))
print("method 2", remove_duplicates2(user_list))
print("method 3", remove_duplicates3(user_list))
