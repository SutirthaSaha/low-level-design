from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def clone(self):
        pass


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def clone(self):
        return Square(self.x, self.y, self.side)

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def clone(self):
        return Circle(self.x, self.y, self.radius)

    def area(self):
        return 3.14 * (self.radius ** 2)


if __name__ == '__main__':
    shape: Shape = Circle(1, 1, 2)
    shape_clone: Shape = shape.clone()

    print(shape.area())
    print(shape_clone.area())

    shape_clone.radius = 3
    print(shape.area())
    print(shape_clone.area())
    print(type(shape), type(shape_clone))
