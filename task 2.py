class NotSleeping:
    """
    The class of a person trying to sleep
    """

    def __init__(self):
        self.sheep_count = 0

    def add_sheep(self):
        """
        A method to help count sheep
        """
        self.sheep_count += 1

person = NotSleeping()
person.add_sheep()
person.add_sheep()
print(person.sheep_count)