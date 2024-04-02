class Dog:
    """
    This class represents a dog.
    """

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def say(self):
        print("Гав!")

my_dog = Dog("Шарик", "Двортерьер", 3)
my_dog.say()
