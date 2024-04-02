class Point:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def get_x(self):
        """
        Method that outputs the value x
        """
        return self.x

    def get_y(self):
        """
        Method that outputs the value y
        """
        return self.y

    def distance(self, other):
        """
        Method that outputs the distance between points
        """
        return (((other.get_x() - self.x)**2) + ((other.get_y() - self.y)**2))**(0.5)

    def sum(self, other):
        """
        Method that outputs coordinates as the sum of the corresponding coordinates of the other and self points.
        """
        new_x = self.x + other.get_x()
        new_y = self.y + other.get_y()
        return f'{(new_x, new_y)}'

    def __str__(self):
        return f'{self.x, self.y}'



point1 = Point((3, 4))
point2 = Point((1, 2))
print(point1.distance(point2))
print(point1.sum(point2))