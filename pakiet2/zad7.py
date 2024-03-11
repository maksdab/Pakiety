from itertools import groupby

numbers = [x for x in  range(15)]


sort_numbers = sorted(numbers, key=lambda x: x % 2)

group_numbers = groupby(sort_numbers, key=lambda x: x % 2)

for key, group in group_numbers:
    if key == 0:
        parzyste = list(group)
        print("Parzyste:", parzyste)
    else:
        nieparzyste = list(group)
        print("Nieparzyste:", nieparzyste)