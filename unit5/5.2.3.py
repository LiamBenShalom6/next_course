from itertools import combinations

def calculate_options():
    bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    target_amount = 100

    options = set()
    for r in range(1, len(bills) + 1):
        for combination in combinations(bills, r):
            if sum(combination) == target_amount:
                options.add(tuple(sorted(combination)))

    return options

def main():
    options = calculate_options()
    for option in options:
        print(option)

    print("Total options:", len(options))

if __name__ == '__main__':
    main()