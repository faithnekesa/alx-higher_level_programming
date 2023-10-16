#!/usr/bin/python3
"""Definition of a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the new Square

        Args:
            size (int): Size of the new Square
            x (int): x coordinate of the new Square
            y (int): y coordinate of the new Square
            id (int): Identifier of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the square size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Function that updates the Square

        Args:
            *args (ints): New attr values
                - 1st arg reps id attr
                - 2nd arg reps size attr
                - 3rd arg reps x attr
                - 4th arg reps y attr
            **kwargs (dict): New key/value pair of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the square dictionary representation"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

