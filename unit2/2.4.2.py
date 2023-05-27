class BigThing:

    def __init__(self, random):
        self._random = random

    def size(self):
        if isinstance(self._random, int):
            return self._random
        return len(self._random)

class BigCat(BigThing):

    def __init__(self, random, weight):
        super().__init__(random)
        self._weight = weight

    def size(self):
        if (self._weight > 20):
            print("Very Fat")
        elif ((self._weight < 20) and (self._weight > 15)):
            print("Fat")
        else:
            print("OK")

my_thing = BigThing("balloon")
print(my_thing.size())

cutie = BigCat("mitzy", 22)
print(cutie.size())