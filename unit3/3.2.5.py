def read_file(file_name):
    str = "__CONTENT_START__\n"
    try:
        file = open(file_name, "r")
    except:
        str += "__NO_SUCH_FILE__\n"
    else:
        for line in file.readlines():
            str += line
    finally:
        str += "__CONTENT_END__"
        return str


def main():
    print(read_file("lll"))
    print()
    print(read_file(r"C:\Users\Liam\PycharmProjects\pythonProject\venv\next_course\names.txt"))


if __name__ == '__main__':
    main()