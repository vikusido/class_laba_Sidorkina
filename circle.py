from shapes import Shapes


class Circle(Shapes):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius is invalid.")
        super().__init__(0, [], [radius])
        self.radius = radius
        self.name = "Circle."

    def get_sq(self):
        return 3.14 * self.radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def get_info(self):
        print(f"Name of the shape: {self.name}.")
        print(f"Radius: {self.radius}.")
        print(f"Perimeter: {self.get_perimeter()}.")
        print(f"Square: {self.get_sq()}.")
