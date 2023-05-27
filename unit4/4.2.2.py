def parse_ranges(ranges_string):
    lst = []
    first_generator = (i.split("-") for i in ranges_string.split(","))
    for start, stop in first_generator:
        for num in range(int(start), int(stop) + 1):
            lst.append(num)
    return (i for i in lst)


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))

if __name__ == '__main__':
    main()