def get_fibo():
    x1 = 0
    x2 = 1
    yield x1
    yield x2
    while True:
        next = x1 + x2
        yield next
        x1 = x2
        x2 = next


def main():
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))

if __name__ == '__main__':
    main()