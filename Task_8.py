# Task 8
# Create a Rectangle class whose attributes will be the height and width of
# the figure. Implement methods to measure the perimeter and area of a
# rectangle.
# Then create a Square class, remembering that every square is a
# rectangle, but not every rectangle is a square.

class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_area(self):
        return self.height * self.width

if __name__ == '__main__':

    r1 = Rectangle(6, 9)
    print(r1.get_perimeter())
    print(r1.get_area())


class Square(Rectangle):

    def __init__(self, side):
        self.side = side

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2


s1 = Square(10)
print(s1.get_perimeter())
print(s1.get_area())