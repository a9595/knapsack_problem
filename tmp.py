from itertools import compress, product

__author__ = 'tieorange'

# sizes = [3, 10, 10, 1, 6, 5, 5, 4, 2, 7, 9, 9, 8, 2, 1, 5, 4, 1, 9, 8, 2, 8, 7, 3, 10, 7]
# values = [7, 7, 16, 11, 6, 3, 1, 15, 3, 8, 3, 13, 11, 15, 8, 13, 2, 12, 14, 1, 2, 18, 9, 8, 19, 5]
sizes = [3, 10, 10, 1]
vals = [7, 7, 16, 11]
LENGTH = len(sizes)
CAPACITY = 40



#
# def per(n):
#     for index in range(1 << n):
#         s = bin(index)[2:]
#         s = '0' * (n - len(s)) + s
#         print(map(int, list(s)))
#
#
# per(3)



def get_char_vector(count):
    char_vector = list()
    for i in product([0, 1], repeat=count):
        char_vector.append(i)
    return char_vector


def calc_list_vector_price(vector_list):
    for vector in vector_list:
        calc_list_vector_price(vector, sizes, vals)


def totalvalue(tmp_list):
    sum_size = 0
    sum_val = 0
    for i, (size, value) in enumerate(tmp_list):
        sum_val += value
        sum_size += size
    CAPACITY = 40
    return sum_val if sum_size <= CAPACITY else (0, 0)


def calc_vector_price(vector, sizes, values):
    tmp_list = list()
    for idx, val in enumerate(vector):
        if val == 1:
            tmp_list.append((sizes[idx], values[idx]))
    return totalvalue(tmp_list)


res = calc_vector_price([0, 0, 1, 1], sizes, vals)


print(res)
