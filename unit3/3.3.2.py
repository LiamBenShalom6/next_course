class UnderAge(Exception):

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return ("The age %d is less than 18, in %d years you will be able to reach Ido's birthday" % (self._arg, 18 -
                                                                                                      self._arg))

    def get_arg(self):
        return self._arg

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)

def main():
    send_invitation("liam", 17)
    send_invitation("lian", 18)



if __name__ == '__main__':
    main()