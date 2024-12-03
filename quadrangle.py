from shapes import Shapes
import math


class Quadrangle(Shapes):
    def __init__(self, a, b, c, d, angles=None, height=None):
        if not all(x > 0 for x in [a, b, c, d]):  # check sides
            raise ValueError("Quadrangle must have four sides.")
        super().__init__(4, angles, [a, b, c, d])
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.angles = angles if angles else []
        self.height = height
        self.name = ""
        if len(self.angles) == 3:  # add an angle if it is not provided
            self.angles.append(360 - sum(self.angles))

    def get_perimeter(self):
        return sum(self.sides) if self.sides else 0

    # definition of figures
    def is_square(self):
        return len(self.sides) == 4 and all(s == self.sides[0] for s in self.sides) and all(
            angle == self.angles[0] for angle in self.angles)

    def is_rectangle(self):
        return len(self.sides) == 4 and len(self.angles) == 4 and all(angle == 90 for angle in self.angles) and \
            self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]

    def is_parallelogram(self):
        return len(self.sides) == 4 and len(self.angles) == 4 and self.sides[0] == self.sides[2] and self.sides[1] == \
            self.sides[3] and self.sides[0] != self.sides[1] and self.sides[2] != self.sides[3]

    def is_rhombus(self):
        return len(self.sides) == 4 and all(s == self.sides[0] for s in self.sides)

    def is_trapezoid(self):
        if len(self.sides) != 4:
            raise ValueError("Four sides are required to define a quadrilateral.")
        for i in range(len(self.angles) - 1):
            if self.angles[i] + self.angles[i + 1] != 180:
                return False
        return True

    # counting square
    def sq_parallelogram_rhombus(self):
        if not self.angles or len(self.angles) != 4:
            raise ValueError("Four angles are required for this calculation.")
        gamma = math.radians(self.angles[0])
        sq = self.a * self.b * math.sin(gamma)
        return sq

    def sq_trapezoid(self):
        if self.height is None or self.height <= 0:
            raise ValueError("Height must be provided and positive for base-height calculation.")
        if abs(self.a - self.c) >= self.height:
            raise ValueError(
                "Provided dimensions are not consistent with a trapezoid (a and c are likely not parallel).")
        sq = 0.5 * (self.a + self.c) * self.height
        return sq

    def get_sq(self, shape_type):
        if shape_type == "square":
            return self.sides[0] ** 2
        elif shape_type == "rectangle":
            return self.sides[0] * self.sides[1]
        elif shape_type == "parallelogram":
            return self.sq_parallelogram_rhombus()
        elif shape_type == "rhombus":
            return self.sq_parallelogram_rhombus()
        elif shape_type == "trapezoid":
            return self.sq_trapezoid()
        else:
            return False

    # get a square and the name of fig
    def fig(self):
        if self.is_square():
            area = self.get_sq("square")
            self.name = "square"

        elif self.is_rectangle():
            area = self.get_sq("rectangle")
            self.name = "rectangle"

        elif self.is_parallelogram():
            area = self.get_sq("parallelogram")
            self.name = "parallelogram"

        elif self.is_rhombus():
            area = self.get_sq("rhombus")
            self.name = "rhombus"

        elif self.is_trapezoid():
            area = self.get_sq("trapezoid")
            self.name = "trapezoid"

        else:
            raise ValueError("Unknown quadrilateral type.")
        print(f"It is a {self.name} with an area of {area}.")

    def get_info(self):
        super().get_info()

    def set_angles(self, new_angles):
        if not all(0 < angle < 360 for angle in new_angles):
            raise ValueError("All angles must be between 0 and 360 degrees.")
        if len(new_angles) == 3:
            new_angles.append(360 - sum(new_angles))
        if sum(new_angles) != 360:
            raise ValueError("The sum of angles of a quadrilateral must be 360 degrees.")
        self.angles = new_angles
        print("Angles updated successfully.")

    def set_sides(self, new_sides):
        if len(new_sides) != self.n_angles:
            raise ValueError(f"Expected {self.n_angles} sides, but got {len(new_sides)}.")
        if not all(side >= 0 for side in new_sides):
            raise ValueError("All sides must be non-negative.")
        self.sides = new_sides
        print("Sides updated successfully.")
