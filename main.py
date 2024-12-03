from circle import Circle
from triangle import Triangle
from quadrangle import Quadrangle
from nangle import Nangle

if __name__ == "__main__":
    try:
        circle = Circle(5)  # set a circle
        circle.get_info()
        print("-----")
        tr1 = Triangle(3, 4, 5)  # set a triangle and square only by Heron's square
        tr1.get_info()
        tr1.heron_square()
        print("-----")
        tr2 = Triangle(3, 4, 5, height=4)  # set a triangle with a height and base square
        tr2.get_info()
        tr2.height_square()
        print("-----")
        tr3 = Triangle(3, 4, 5, angles=[45, 60, 75],
                       height=6)  # set a triangle with 3 types of a square, it has different values as height and angles are written
        tr3.get_info()
        tr3.heron_square()
        tr3.height_square()
        tr3.angles_square()

        # print("-----")
        # tr4 = Triangle(10, 4, 5, angles=[45, 45, 90], height=4)  # incorrect triangle
        # tr4.get_sq()
        # tr4.get_info()
        print("-----")
        fig1 = Quadrangle(3, 4, 5, 6, angles=[90, 90, 90, 90], height=3)  # trapezoid
        fig1.get_info()
        fig1.fig()
        print("-----")
        fig2 = Quadrangle(3, 3, 3, 3, angles=[90, 90, 90, 90], height=3)  # square
        fig2.get_info()
        fig2.fig()
        print("-----")
        fig3 = Quadrangle(3, 4, 3, 4, angles=[90, 90, 90, 90], height=3)  # rectangle
        fig3.get_info()
        fig3.fig()
        print("-----")
        fig4 = Quadrangle(4, 4, 4, 4, angles=[90, 110, 80, 80], height=3)  # rhombus
        fig4.get_info()
        fig4.fig()
        print("-----")
        fig5 = Quadrangle(3, 4, 3, 4, angles=[60, 120, 60, 120], height=3)  # parallelogram
        fig5.get_info()
        fig5.fig()
        print("-----")
        fig6 = Quadrangle(13, 2, 3, 10, angles=[40, 60, 100, 160])  # unknown figure
        fig6.set_sides([4, 5, 6, 7])
        fig6.set_angles([80, 90, 80, ])  # to show the work of set_angles
        fig6.get_info()
        fig6.fig()
        print("-----")
        pent = Nangle("Pentagon", 5, [60, 120, 50, 170, 140], [13, 14, 15, 20, 17])  # pentagon
        pent.get_info()
    except ValueError as ex:
        print(f"Error: {ex}")
