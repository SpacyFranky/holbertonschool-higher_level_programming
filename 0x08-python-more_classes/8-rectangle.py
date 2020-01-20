#!/usr/bin/python3
"""
Real definition of a rectangle.
Calculates area and parameter.
"""


class Rectangle:
    """A definition of a rectangle.
    Args:
        width (int): width of the Rectangle.
        height (int): height of the Rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return("")
        else:
            s = (self.width * str(self.print_symbol) + "\n") * self.height
            s = s[:-1]
            return(s)

    def __repr__(self):
        return("Rectangle("+str(self.width)+", "+str(self.height)+")")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        else:
            return((self.width + self.height) * 2)

    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return(rect_1)
        elif rect_1.area() > rect_2.area():
            return(rect_1)
        else:
            return(rect_2)
