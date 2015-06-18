sizes = [3, 10, 10, 1, 6]
vals = [7, 7, 16, 11, 6]
LENGTH = len(sizes)
CAPACITY = 40


def get_binary_string(number):
    binary = "{:0b}".format(number)
    print("type of binary = ", type(binary))
    print("binary = ", binary)

    return binary


def convert_bin_to_long(binary_str):
    integer_bin_arr = [None] * LENGTH
    for idx in range(LENGTH):
        try:
            integer_bin_arr[idx] = int(binary_str[idx])
        except IndexError:
            integer_bin_arr[idx] = 0
    return integer_bin_arr


#  ---------WORKS

#  [0, 0, 1, 1]
def convert_to_bin_divide_by_2(dec_number):
    integer_bin_arr = [0] * LENGTH
    idx = LENGTH - 1

    while dec_number > 0:
        rem = dec_number % 2
        integer_bin_arr[idx] = rem
        idx -= 1
        dec_number //= 2
    return integer_bin_arr


#  [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0].....]
def get_char_vector_matrix():
    char_vectors_list = list()
    for i in range(2 ** LENGTH):
        converted_dec_to_bin = convert_to_bin_divide_by_2(i)
        char_vectors_list.append(converted_dec_to_bin)
    return char_vectors_list


def calc_vector_price(vector):
    tmp_list = list()
    for idx, val in enumerate(vector):
        if val == 1:
            tmp_list.append((sizes[idx], vals[idx]))
    return get_val_sum(tmp_list)


def get_val_sum(tmp_list):
    sum_size = 0
    sum_val = 0
    for i, (size, value) in enumerate(tmp_list):
        sum_val += value
        sum_size += size
    return sum_val if sum_size <= CAPACITY else 0


def calc_WHOLE_char_vector(char_vector_matrix):
    result_values = list()
    for vector in char_vector_matrix:
        sum_value_of_vector = calc_vector_price(vector)
        result_values.append(sum_value_of_vector)
    return result_values

def print_the_best_vector_items(the_best_vector):
    for idx, val in enumerate(the_best_vector):
        if val == 1:
            print("item #", idx, "  val =  ", vals[idx], "\t size = ", sizes[idx])


char_vector_matrix = get_char_vector_matrix()
print(char_vector_matrix)

sum_values_list = calc_WHOLE_char_vector(char_vector_matrix)
print(sum_values_list)

max_value = max(sum_values_list)
max_index = sum_values_list.index(max_value)

the_best_vector = char_vector_matrix[max_index]

print("max val = ", max_value)
print("max idx = ", max_index)

print("so the best vector is", the_best_vector)
print_the_best_vector_items(the_best_vector)




#  ----------------
# binary_result = get_binary_string(13)
# # iterate_binary(binary_result)
# # print("str[2] = %d" % int(binary_result[2]))
#
# long = convert_bin_to_long(binary_result)
# print(long)
# print(type(long))
