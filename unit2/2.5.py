class Animal:
    """
    A class representing an animal.
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        Initialize an Animal object.

        Args:
            name (str): The name of the animal.
            hunger (int): The hunger level of the animal (default is 0).
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Get the name of the animal.

        Returns:
            str: The name of the animal.
        """
        return self._name

    def is_hungry(self):
        """
        Check if the animal is hungry.

        Returns:
            bool: True if the animal is hungry, False otherwise.
        """
        return self._hunger > 0

    def feed(self):
        """
        Feed the animal by decreasing its hunger level by 1.
        """
        self._hunger -= 1

    def talk(self):
        """
        Make the animal talk.
        """
        print("I talk like an animal")

    def __str__(self):
        """
        Return a string representation of the animal.

        Returns:
            str: A string representation of the animal.
        """
        return "My name is {} and I am an animal!".format(self._name)


class Dog(Animal):
    """
    A class representing a dog, which is a type of animal.
    """

    def talk(self):
        """
        Make the dog bark.
        """
        print("Woof woof")

    def fetch_stick(self):
        """
        Make the dog fetch a stick.
        """
        print("There you go, sir!")

    def __str__(self):
        """
        Return a string representation of the dog.

        Returns:
            str: A string representation of the dog.
        """
        return "My name is {} and I am a dog!".format(self._name)


class Cat(Animal):
    """
    A class representing a cat, which is a type of animal.
    """

    def talk(self):
        """
        Make the cat meow.
        """
        print("Meow")

    def chase_laser(self):
        """
        Make the cat chase a laser.
        """
        print("Meeeeow")

    def __str__(self):
        """
        Return a string representation of the cat.

        Returns:
            str: A string representation of the cat.
        """
        return "My name is {} and I am a cat!".format(self._name)


class Skunk(Animal):
    """
    A class representing a skunk, which is a type of animal.
    """

    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initialize a Skunk object.

        Args:
            name (str): The name of the skunk.
            hunger (int): The hunger level of the skunk (default is 0).
            stink_count (int): The stink count of the skunk (default is 6).
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        Make the skunk make a hissing sound.
        """
        print("Tsssss")

    def stink(self):
        """
        Make the skunk emit a stinky smell.
        """
        print("Dear lord!")

    def __str__(self):
        """
        Return a string representation of the skunk.

        Returns:
            str: A string representation of the skunk.
        """
        return "My name is {} and I am a skunk!".format(self._name)

class Unicorn(Animal):
    """
    A class representing a unicorn, which is a type of animal.
    """

    def talk(self):
        """
        Make the unicorn say a greeting.
        """
        print("Good day, darling")

    def sing(self):
        """
        Make the unicorn sing a song.
        """
        print("I'm not your toy...")

    def __str__(self):
        """
        Return a string representation of the unicorn.

        Returns:
            str: A string representation of the unicorn.
        """
        return "My name is {} and I am a unicorn!".format(self._name)


class Dragon(Animal):
    """
    A class representing a dragon, which is a type of animal.
    """

    def __init__(self, name, hunger=0, color="Green"):
        """
        Initialize a Dragon object.

        Args:
            name (str): The name of the dragon.
            hunger (int): The hunger level of the dragon (default is 0).
            color (str): The color of the dragon (default is "Green").
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        Make the dragon roar.
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        Make the dragon breathe fire.
        """
        print("$@#$#@$")

    def __str__(self):
        """
        Return a string representation of the dragon.

        Returns:
            str: A string representation of the dragon.
        """
        return "My name is {} and I am a dragon!".format(self._name)


def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky")
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)

    dog1 = Dog("Doggo", 80)
    cat1 = Cat("Kitty", 80)
    skunk1 = Skunk("Stinky Jr.")
    unicorn1 = Unicorn("Clair", 80)
    dragon1 = Dragon("McFly", 80)

    zoo_lst = [dog, cat, skunk, unicorn, dragon, dog1, cat1, skunk1, unicorn1, dragon1]

    for animal in zoo_lst:
        print(" ")
        print(animal)
        while animal.is_hungry():
            animal.feed()
        animal.talk()

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == '__main__':
    main()