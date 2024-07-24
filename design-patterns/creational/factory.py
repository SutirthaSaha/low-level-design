from abc import ABC, abstractmethod
from enum import Enum


class Toy(ABC):
    @abstractmethod
    def play(self):
        pass


class Tank(Toy):
    def play(self):
        print("Play with tank")


class Barbie(Toy):
    def play(self):
        print("Play with barbie")


class ToyType(Enum):
    TANK = "Tank"
    BARBIE = "Barbie"


class ToyFactory:
    def create(self, toy_type: ToyType):
        if toy_type == ToyType.TANK.value:
            return Tank()
        elif toy_type == ToyType.BARBIE.value:
            return Barbie()
        else:
            raise Exception("Invalid toy type")


if __name__ == '__main__':
    toy_factory = ToyFactory()
    toy_type = "Tank"
    toy = toy_factory.create(toy_type)
    toy.play()
