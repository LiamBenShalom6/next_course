import functools

def four_dividers(number):
    return list(filter(check_if_four_divider, range(1, number + 1)))


def check_if_four_divider(number):
    return number % 4 == 0



def main():
    print(four_dividers(20))
    print(four_dividers(9))
    print(four_dividers(3))


if __name__ == '__main__':
    main()