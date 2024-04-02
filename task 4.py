class User:
    """
    User data class
    """
    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        """
        A method that updates user information
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender


    def __str__(self):
        return f"{self.first_name} {self.id} ({self.nick_name})"

user1 = User(1, "user123", "Alice")
print(user1)

user1.update(1, "bob", "dfghj")
print(user1)
