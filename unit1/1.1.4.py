import functools

def sum_of_digits(number):
    return functools.reduce(add, list(str(number)))

def add(num1, num2):
    return int(num1) + int(num2)

def main():
    print(sum_of_digits(104))


if __name__ == '__main__':
    main()

