from triangle import Triangle
from polygon import Polygon
from geometricObject import GeometricObject

def main():
    outfile = open("results.txt", 'w')
    outfile.write("list of wrong geometric objects:\n")
    l = []
    try:
      l.append(Triangle(name="triangle 3", \
                   a=3.5, b=4.5, c=8, \
                   color="green", filled=True))
    except ValueError as e:
      outfile.write(str(e))
    try:
      l.append(Triangle(name = "triangle 1"))
    except ValueError as e:
      outfile.write(str(e))
    try:
      l.append(Triangle(name = "triangle 2", a=3, b=3, c=3))
    except ValueError as e:
      outfile.write(str(e))
    try:
      l.append(Triangle(name = "triangle 5", a=2, b=3, c=3))
    except ValueError as e:
      outfile.write(str(e))
    try:
      l.append(Triangle(name = "triangle 4", a=7, b=5, c=4,\
                    color = "Red", filled = True))
    except ValueError as e:
      outfile.write(str(e))
    try:
      l.append(Triangle(name="triangle 6", a=1, b=2, c=3, \
                   color="Yellow", filled=True))
    except ValueError as e:
      outfile.write(str(e))
    try:
          l.append(Polygon(name="polygon 2", \
               numberOfSides = 4, shape = "square", \
               color="Purple", filled=True))
    except ValueError as e:
          outfile.write(str(e))
    try:
        l.append(Polygon(name="polygon 1"))
    except ValueError as e:
        outfile.write(str(e))
    try:
        l.append(GeometricObject(name="geometric object 1", \
          filled = True, color = "blue", shape = "circle"))
    except ValueError as e:
        outfile.write(str(e))

    outfile.write(
      "\n\nlist of correct geometric objects\n"
            + "    sorted by shape (primary sort)\n"
            + "          and name (secondary sort):\n")

    pass # change it

    for o in l:
      o.writeObject(outfile)
      outfile.write("\n")


    outfile.close()

main() # Call the main function
