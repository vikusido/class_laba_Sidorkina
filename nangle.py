from shapes import Shapes


class Nangle(Shapes):
    def __init__(self, name, n_angles, angles, sides):
        super().__init__(n_angles, angles, sides)
        self.name = name
        if not angles and not sides:
            raise ValueError("Nangle must have either angles or sides defined.")
        if angles and sides and len(angles) != len(sides):
            raise ValueError("Number of angles and sides must be equal.")

    def get_info(self):
        super().get_info()
        print(f"Name: {self.name}.")

