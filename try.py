from itertools import product

binary = '{:02b}'.format(2)
print(binary)
LENGTH = 5


def get_binary_string(number):
    binary = "{:05b}".format(number)
    print("type of binary = ", type(binary))

    return binary


get_binary_string(2)


def get_new_char_vector():
    final_vector = list()
    tmp_vector = list()
    size = 2 ** LENGTH
    for i in range(0, size - 1):
        bin_vector = get_binary_string(i)
        for element in bin_vector:
            tmp_vector.append(int(element))
        final_vector.append(tmp_vector)
    return final_vector


bin_vector = get_binary_string(5)
print(bin_vector[0])

vector = get_new_char_vector()
print(bin_vector[0])
print(vector[0])


def get_char_vector(count):
    char_vector = list()
    for i in product([0, 1], repeat=count):
        char_vector.append(list(i))
    return char_vector


print(get_char_vector(5))
