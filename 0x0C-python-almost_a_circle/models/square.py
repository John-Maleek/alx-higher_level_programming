#!/usr/bin/python3
"""Module defines a Square class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the value of a private attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of a private  attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of Square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """Updates parameters of class instance"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Retuns a dictionary representation of the class"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
