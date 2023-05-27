def is_funny(string):
    return len([x for x in string if x != 'h' and x != 'a']) == 0

def main():
    print(is_funny("hhahahzzzahaha"))


if __name__ == '__main__':
    main()