def intersection(list_1, list_2):
    lst = []
    [lst.append(x) for x in list_1 for y in list_2 if y == x if y not in lst]
    return lst

def main():
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


if __name__ == '__main__':
    main()