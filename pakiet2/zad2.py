from itertools import combinations

def generate_combinations(elements):
    return list(combinations(elements, 2))

elements = ['A', 'B', 'C', 'D']
combo = generate_combinations(elements)

print(combo)