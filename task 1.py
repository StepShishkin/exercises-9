class Dog:
    """
    This class represents a dog.

    Attributes:
    - name (str): the name of the dog
    - breed (str): the breed of the dog
    - age (int): the age of the dog
    """

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def say(self):
        print("Гав!")

my_dog = Dog("Шарик", "Двортерьер", 3)
my_dog.say()