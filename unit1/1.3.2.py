def is_prime(number):
    return len([num for num in range(2, number) if number % num == 0]) == 0

def main():
    print(is_prime(42))
    print(is_prime(43))


if __name__ == '__main__':
    main()

