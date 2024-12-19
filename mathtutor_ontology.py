from owlready2 import *

# Create a new ontology
onto = get_ontology("http://example.org/mathtutor")

with onto:
    # Define Classes
    class Shape(Thing):
        pass

    class HasArea(Shape >> float):
        pass

    class Square(Shape):
        pass

    class Rectangle(Shape):
        pass

    class Triangle(Shape):
        pass

    # Define Relationships
    class HasSide(Square >> float):
        pass

    class HasLength(Rectangle >> float):
        pass

    class HasWidth(Rectangle >> float):
        pass

    class HasBase(Triangle >> float):
        pass

    class HasHeight(Triangle >> float):
        pass

# Create Instances
sq = Square("Square1")
sq.HasSide = [5]
sq.HasArea = [sq.HasSide[0] ** 2]

rec = Rectangle("Rectangle1")
rec.HasLength = [10]
rec.HasWidth = [4]
rec.HasArea = [rec.HasLength[0] * rec.HasWidth[0]]

tri = Triangle("Triangle1")
tri.HasBase = [8]
tri.HasHeight = [6]
tri.HasArea = [0.5 * tri.HasBase[0] * tri.HasHeight[0]]

# Save the ontology
onto.save(file="mathtutor.owl", format="rdfxml")

print(f"{sq.name} area: {sq.HasArea[0]}")
print(f"{rec.name} area: {rec.HasArea[0]}")
print(f"{tri.name} area: {tri.HasArea[0]}")
