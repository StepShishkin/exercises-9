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

    def lost(self):
        """
        The method of losing count
        """
        self.sheep_count = 0

    def get_count_sheep(self):
        """
        Method for displaying the current number of sheep
        """
        return self.sheep_count

person = NotSleeping()
person.add_sheep()
person.add_sheep()
person.lost()
person.add_sheep()
print(person.get_count_sheep())