def double_letter(my_str):
    return "".join(list(map(miror, list(my_str))))

def miror(char):
    return char * 2

def main():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))


if __name__ == '__main__':
    main()