def combine_coins(coin, numbers):
    list_of_numbers_with_coin = [str(num) + coin for num in numbers]
    return ", ".join(list_of_numbers_with_coin)

def main():
    print(combine_coins('$', range(5)))


if __name__ == '__main__':
    main()