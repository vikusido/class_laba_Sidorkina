import math


class Shapes:
    def __init__(self, n_angles, angles=None, sides=None):
        if angles is None:
            angles = []
        if sides is None:
            sides = []
        if n_angles < 0:
            raise ValueError("Number of angles cannot be negative.")
        if angles and len(angles) != n_angles:
            raise ValueError("Number of angles must match n_angles.")

        # check the value of angles
        if angles:
            for angle in angles:
                if angle <= 0 or angle >= 360:
                    raise ValueError("Angles must be positive and less than 360 degrees.")
        if angles and len(angles) > 0:
            total_angles = sum(angles)
            expected_sum = (n_angles - 2) * 180
            if abs(total_angles - expected_sum) > 1e-6:
                raise ValueError(f"Angles do not add up to (n-2)*180 = {expected_sum}")

        # check the value of sides
        if sides:
            for side in sides:
                if side <= 0:
                    raise ValueError("Side lengths cannot be negative or zero.")
        self.n_angles = n_angles
        self.angles = angles
        self.sides = sides

    def get_perimeter(self):
        return sum(self.sides) if self.sides else 0

    def get_info(self):
        print(f"Angles: {self.angles}")
        print(f"Sides: {self.sides}")
        print(f"Perimeter: {self.get_perimeter()}")

    def set_angles(self, new_angles):
        if not all(0 < angle < 360 for angle in new_angles):
            raise ValueError("All angles must be between 0 and 360 degrees.")
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
