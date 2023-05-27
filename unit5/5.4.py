class IDIterator:
    """Iterator class that generates the next valid ID number in the range."""

    def __init__(self, id_):
        """
        Initialize the IDIterator instance.

        Args:
            id_ (int): The starting ID number.
        """
        self._id = id_

    def __iter__(self):
        """
        Return the iterator instance.

        Returns:
            IDIterator: The iterator instance.
        """
        return self

    def __next__(self):
        """
        Return the next valid ID number.

        Returns:
            int: The next valid ID number.

        Raises:
            StopIteration: If the ID number exceeds the upper limit.
        """
        self._id += 1
        if self._id > 999999999:
            raise StopIteration
        while not check_id_valid(self._id):
            self._id += 1
        if self._id > 999999999:
            raise StopIteration
        return self._id


def check_id_valid(id):
    """
    Check if the ID number is valid.

    Args:
        id (int): The ID number to check.

    Returns:
        bool: True if the ID number is valid, False otherwise.
    """
    index = 1
    res = list(map(int, str(id)))
    list_first_level = []

    for i in res:
        if index % 2 == 0:
            list_first_level.append(i * 2)
        else:
            list_first_level.append(i)
        index += 1
    list_second_level = [x if x < 10 else x // 10 + x % 10 for x in list_first_level]
    sum_of_id = sum(list_second_level)
    return sum_of_id % 10 == 0


def id_generator(id_):
    """
    Generator function that generates the next valid ID number.

    Args:
        id_ (int): The starting ID number.

    Yields:
        int: The next valid ID number.
    """
    while True:
        id_ += 1
        while not check_id_valid(id_):
            id_ += 1
        if id_ < 999999999:
            yield id_


def main():
    """Main function to run the program."""
    id_ = int(input("Enter ID: "))
    type_ = input("Generator or Iterator? (gen/it): ")
    if type_ == "gen":
        print("I'm in generator!")
        id_gen = id_generator(id_)
        count = 0
        for i in id_gen:
            if count < 10:
                print(i)
                count += 1
            else:
                break
    elif type_ == "it":
        print("I'm in iterator!")
        id_iterator = IDIterator(id_)
        for _ in range(10):
            print(next(id_iterator))


if __name__ == '__main__':
    main()