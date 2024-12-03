from shapes import Shapes
import math


class Triangle(Shapes):
    def __init__(self, a, b, c, angles=None, height=None):
        if not all(x > 0 for x in [a, b, c]):  # check sides
            raise ValueError("Side lengths must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:  # check sides
            raise ValueError("Triangle inequality violated.")
        super().__init__(3, angles, [a, b, c])
        self.a = a
        self.b = b
        self.c = c
        self.angles = angles if angles else []
        self.height = height
        self.name = "Triangle"
        if len(self.angles) == 2:  # add an angle if it is not provided
            self.angles.append(180 - sum(self.angles))

    def get_perimeter(self):
        return sum(self.sides) if self.sides else 0

    def heron_square(self):
        p = (self.a + self.b + self.c) / 2
        sq = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f"Heron's square: {sq}")
        return sq

    def height_square(self):
        if self.height is None or self.height <= 0:
            raise ValueError("Height must be provided and positive for base-height calculation.")
        sq = 0.5 * self.height * self.a
        print(f"Square with a height and a base: {sq}")
        return sq

    def angles_square(self):
        if not self.angles or len(self.angles) != 3:
            raise ValueError("Three angles are required for this calculation.")
        gamma = math.radians(self.angles[0])
        sq = 0.5 * self.a * self.b * math.sin(gamma)
        print(f"Square with angles: {sq}")
        return sq

    def get_sq(self):
        try:
            return self.heron_square()
        except ValueError:
            try:
                return self.height_square()
            except ValueError:
                try:
                    return self.angles_square()
                except ValueError:
                    return None

    def get_info(self):
        super().get_info()
        print(f"Name of the shape: {self.name}.")

    def set_angles(self, new_angles):
        if not all(0 < angle < 180 for angle in new_angles):
            raise ValueError("All angles must be between 0 and 180 degrees.")
        if len(new_angles) == 2:
            new_angles.append(180 - sum(new_angles))
        if sum(new_angles) != 180:
            raise ValueError("The sum of angles of a quadrilateral must be 180 degrees.")
        self.angles = new_angles
        print("Angles updated successfully.")

    def set_sides(self, new_sides):
        if len(new_sides) != self.n_angles:
            raise ValueError(f"Expected {self.n_angles} sides, but got {len(new_sides)}.")
        if not all(side >= 0 for side in new_sides):
            raise ValueError("All sides must be non-negative.")
        self.sides = new_sides
        print("Sides updated successfully.")
