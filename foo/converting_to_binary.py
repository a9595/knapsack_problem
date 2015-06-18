LENGTH = 10


def get_binary_string(number):
    binary = "{:0b}".format(number)
    print("type of binary = ", type(binary))
    print("binary = ", binary)

    return binary



#  ---------WORKS
def convert_bin_to_long(binary_str):
    integer_bin_arr = [None] * LENGTH
    for idx in range(LENGTH):
        try:
            integer_bin_arr[idx] = int(binary_str[idx])
        except IndexError:
            integer_bin_arr[idx] = 0
    return integer_bin_arr


def divideBy2(decNumber):
    integer_bin_arr = [0] * LENGTH
    idx = LENGTH-1

    while decNumber > 0:
        rem = decNumber % 2
        integer_bin_arr[idx] = rem
        idx -= 1
        decNumber //= 2
    return integer_bin_arr



bin_arr = divideBy2(2)
print(bin_arr)


#  ----------------
# binary_result = get_binary_string(13)
# # iterate_binary(binary_result)
# # print("str[2] = %d" % int(binary_result[2]))
#
# long = convert_bin_to_long(binary_result)
# print(long)
# print(type(long))
