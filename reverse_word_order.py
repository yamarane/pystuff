# python3
# this program takes a line from user and gives back in reverse order.
user_input = input("please enter a line: ")


def reverse_word_order(user_input_line):
    split_line = user_input_line.split()
    result = []
    for word in split_line:
        result.insert(0, word)
    return " ".join(result)
print(reverse_word_order(user_input))
