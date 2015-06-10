CAPACITY = 40
LENGTH = range(0, 26)
sizes = [3, 10, 10, 1, 6, 5, 5, 4, 2, 7, 9, 9, 8, 2, 1, 5, 4, 1, 9, 8, 2, 8, 7, 3, 10, 7]
vals = [7, 7, 16, 11, 6, 3, 1, 15, 3, 8, 3, 13, 11, 15, 8, 13, 2, 12, 14, 1, 2, 18, 9, 8, 19, 5]

best_value = 0;
best_sizes = 0;
best_char_vect = list()


def calculate_solution(characteristic_vector):
    curr_value = 0
    curr_size = 0

    for i in LENGTH:
        curr_value += vals * characteristic_vector[i]
        curr_size += sizes * characteristic_vector[i]
        if curr_size <= CAPACITY:
            if curr_value > b

    pass


def permitation(characteristic_vector, current_length):
    if current_length == 1:
        characteristic_vector[0] = 0
        calculate_solution(characteristic_vector)

        characteristic_vector[0] = 1
        calculate_solution(characteristic_vector)
    else:
        characteristic_vector[current_length] = 0
        permitation(characteristic_vector, current_length - 1)

        characteristic_vector[current_length] = 1
        permitation(characteristic_vector, current_length - 1)
