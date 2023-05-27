numbers = iter(list(range(1, 101)))
next(numbers)
next(numbers)
try:
    for i in numbers:
        print(i)
        next(numbers)
        next(numbers)
except StopIteration:
    pass
