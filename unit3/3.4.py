import string

class UsernameContainsIllegalCharacter(Exception):
    """
    Exception raised when the username contains an illegal character.
    """

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return ('The username contains an illegal character "%s" at index %d' % (self._arg[0], self._arg[1]))

    def get_arg(self):
        return self._arg


class UsernameTooShort(Exception):
    """
    Exception raised when the username is too short (less than 3 characters).
    """

    def __init__(self):
        pass

    def __str__(self):
        return "Username consisting of fewer than 3 characters"

    def get_arg(self):
        return self._arg


class UsernameTooLong(Exception):
    """
    Exception raised when the username is too long (more than 16 characters).
    """

    def __init__(self):
        pass

    def __str__(self):
        return "A username consisting of more than 16 characters"

    def get_arg(self):
        return self._arg


class PasswordMissingCharacter(Exception):
    """
    Exception raised when the password is missing a character.
    """

    def __init__(self):
        pass

    def __str__(self):
        return "The password is missing a character"

    def get_arg(self):
        return self._arg


class PasswordTooShort(Exception):
    """
    Exception raised when the password is too short (less than 8 characters).
    """

    def __init__(self):
        pass

    def __str__(self):
        return "A password consisting of fewer than 8 characters"

    def get_arg(self):
        return self._arg


class PasswordTooLong(Exception):
    """
    Exception raised when the password is too long (more than 40 characters).
    """

    def __init__(self):
        pass

    def __str__(self):
        return "A password consisting of more than 40 characters"

    def get_arg(self):
        return self._arg


class PasswordMissingUppercaseCharacter(PasswordMissingCharacter):
    """
    Exception raised when the password is missing an uppercase character.
    """

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__() + " (Uppercase)"

    def get_arg(self):
        return self._arg


class PasswordMissingLowercaseCharacter(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a lowercase character.
    """

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__() + " (Lowercase)"

    def get_arg(self):
        return self._arg


class PasswordMissingDigitCharacter(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a digit character.
    """

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__() + " (Digit)"

    def get_arg(self):
        return self._arg


class PasswordMissingSpecialCharacter(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a special character.
    """

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__() + " (Special)"

    def get_arg(self):
        return self._arg

def check_input(username, password):
    """
    Checks if the given username and password meet the specified criteria.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        bool: True if the username and password are valid, False otherwise.
    """
    try:
        # Check username
        index = 0
        for letter in username:
            if not ((letter.isnumeric()) or (letter == "_") or (letter.isalpha())):
                raise UsernameContainsIllegalCharacter([letter, index])
            index += 1
        if len(username) < 3:
            raise UsernameTooShort
        elif len(username) > 16:
            raise UsernameTooLong

        # Check password
        if len(password) < 8:
            raise PasswordTooShort
        elif len(password) > 40:
            raise PasswordTooLong

        contain_uppercase_letter = False
        contain_lowercase_letter = False
        contain_number = False
        contain_special_character = False

        for char in password:
            if char in string.ascii_lowercase:
                contain_lowercase_letter = True
            elif char in string.ascii_uppercase:
                contain_uppercase_letter = True
            elif char in string.punctuation:
                contain_special_character = True
            elif char.isnumeric():
                contain_number = True

        if not contain_uppercase_letter:
            raise PasswordMissingUppercaseCharacter
        elif not contain_lowercase_letter:
            raise PasswordMissingLowercaseCharacter
        elif not contain_number:
            raise PasswordMissingDigitCharacter
        elif not contain_special_character:
            raise PasswordMissingSpecialCharacter

    except UsernameContainsIllegalCharacter as e:
        print(e)
        return False

    except UsernameTooShort as e:
        print(e)
        return False

    except UsernameTooLong as e:
        print(e)
        return False

    except PasswordTooShort as e:
        print(e)
        return False

    except PasswordTooLong as e:
        print(e)
        return False

    except PasswordMissingUppercaseCharacter as e:
        print(e)
        return False

    except PasswordMissingLowercaseCharacter as e:
        print(e)
        return False

    except PasswordMissingDigitCharacter as e:
        print(e)
        return False

    except PasswordMissingSpecialCharacter as e:
        print(e)
        return False

    else:
        print("OK")
        return True


def main():
    """
    Entry point of the program.
    Prompts the user to enter a username and password,
    then checks if they meet the specified criteria.
    """
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    while not check_input(username, password):
        username = input("Enter username again: ")
        password = input("Enter password again: ")


if __name__ == '__main__':
    main()