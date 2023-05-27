class Dog:
    count_animals = 0

    def __init__(self, name="dog", age=0):
        self._name = name
        self._age = age
        Dog.count_animals += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

def main():
    first_dog = Dog("krembo", 3)
    second_dog = Dog()

    print("first dog age: " + first_dog.get_name())
    print("first dog age: " + str(first_dog.get_age()))
    print("second dog age: " + second_dog.get_name())
    print("second dog age: " + str(second_dog.get_age()))

    second_dog.set_name("pich")
    print("second dog age: " + str(second_dog.get_name()))
    print("number of animals: " + str(Dog.count_animals))



if __name__ == '__main__':
    main()