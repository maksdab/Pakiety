def lazy_evaluation():
    for i in range(5):
        yield i

gen = lazy_evaluation()

for i in gen:
    print(i)
