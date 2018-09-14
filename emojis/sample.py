def print_string(string, index=0):

    if index < len(string):
        print(string[index])
        index += 1
        print_string(string, index)


print_string('Hello, world!')
