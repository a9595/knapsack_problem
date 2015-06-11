# from itertools import combinations
from itertools import product

sizes = [3, 10, 10, 1]
vals = [7, 7, 16, 11]
LENGTH = len(sizes)

def get_char_vector(count):
    char_vector = list()
    for i in product([0, 1], repeat=count):
        char_vector.append(i)
    return char_vector

def _get_converted_data(sizes, values):
    items = list()
    for i in range(1, len(sizes)):
        items.append((i, sizes[i], values[i]))
    return items





def anycomb(items):
    ' return combinations of any length from the items '
    return (comb for r in range(1, len(items) + 1)
            for comb in combinations(items, r))


def totalvalue(comb):
    ' Totalise a particular combination of items'
    total_weight = total_value = 0
    for item, weight, value in comb:
        total_weight += weight
        total_value += value
    capacity = 40
    return (total_value, -total_weight) if total_weight <= capacity else (0, 0)


items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
)


# items = _get_converted_data(sizes, vals)



combintaions = anycomb(items)

bagged = max(combintaions, key=totalvalue)  # max val or min wt if values equal

print("\t combinations:", combinations)
print("\t bagged:", bagged)
print("Bagged the following items\n  " +
      '\n  '.join(sorted(item for item, _, _ in bagged)))
val, wt = totalvalue(bagged)
print("for a total value of %i and a total weight of %i" % (val, -wt))
