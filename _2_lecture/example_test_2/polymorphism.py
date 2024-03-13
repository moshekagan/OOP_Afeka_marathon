from circle import Circle
from rectangle import Rectangle
from regularPolygon import Square
from regularPolygon import EquilateralTriangle
from regularPolygon import EquilateralPentagon


def main():
    try:
        outfile = open("results.txt", 'w')
        l = [
            Circle(4),
            Rectangle(1, 3),
            Square(10),
            EquilateralTriangle(5),
            EquilateralPentagon(5, "yellow", True)
        ]
        l[0].setRadius(0)
        l[1].setHeight(-1)
        l[1].setWidth(0)

        outfile.write("list of geometric objects before sort:\n")

        for o in l:
            o.writeObject(outfile)

        l.sort(key=lambda shape: shape.getArea(), reverse=True)

        outfile.write("\n\nlist of geometric objects after sort (descending):\n")

        for o in l:
            o.writeObject(outfile)

        outfile.write("\n")

        e = EquilateralTriangle(0)

    except ValueError as e:
        outfile.write(str(e))
    finally:
        outfile.close()


main()  # Call the main function
