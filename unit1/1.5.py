import functools

def max_length_name(names_from_file):
    """
        Find the name with the maximum length from the given list of names.

        Args:
            names_from_file (list): List of names.

        Returns:
            str: The name with the maximum length.
    """

    return max(names_from_file, key= len)
    return " ".join([name for name in names_from_file if len(name) == max_len])

def sum_length(names_from_file):
    """
        Calculate the sum of the lengths of all names in the given list.

        Args:
            names_from_file (list): List of names.

        Returns:
            int: The sum of the lengths of all names.
    """

    return functools.reduce(lambda x, y: x + y, map(lambda x : len(x), names_from_file))

def min_length_name(names_from_file):
    """
        Find the names with the minimum length from the given list of names.

        Args:
            names_from_file (list): List of names.

        Returns:
            str: The names with the minimum length (each name on a separate line).
    """

    min_length = min(list(map(lambda x : len(x), names_from_file)))
    return "\n".join([name for name in names_from_file if len(name) == min_length])

def name_length(names_from_file):
    """
        Write the lengths of all names from the given list to a file.

        Args:
            names_from_file (list): List of names.
    """
    input_name_length_file = open(r"C:\Users\Liam\PycharmProjects\pythonProject\venv\next_course\name_length.txt", 'w')
    input_name_length_file.write("\n".join(list(map(lambda x: str(len(x)), names_from_file)))
)
    input_name_length_file.close()

def names_in_length(names_from_file):
    """
        Find the names in the given list with a specific length.

        Args:
            names_from_file (list): List of names.

        Returns:
            str: The names with the specified length (each name on a separate line).
    """

    length = int(input("Enter name length: "))
    return "\n".join([name for name in names_from_file if len(name) == length])

def main():
    input_file = open(r"C:\Users\Liam\PycharmProjects\pythonProject\venv\next_course\names.txt", 'r')

    names_from_file = [x.replace("\n", "") for x in input_file.readlines()]
    print(max_length_name(names_from_file))
    print(sum_length(names_from_file))
    print(min_length_name(names_from_file))
    name_length(names_from_file)
    print(names_in_length(names_from_file))

    input_file.close()



if __name__ == '__main__':
    main()