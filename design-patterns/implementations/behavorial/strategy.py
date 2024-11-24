from abc import ABC, abstractmethod


class Multiply(ABC):
    @abstractmethod
    def operate(self, a: int, b: int):
        pass


class MultiplyByAddition(Multiply):
    def operate(self, a:int, b:int):
        print("Multiply by addition")
        product = 0
        for _ in range(b):
            product = product + a
        return product


class MultiplyByMultiplication(Multiply):
    def operate(self, a:int, b:int):
        print("Multiply by multiplication")
        return a * b


class Calculate:
    def __init__(self, multiply_strategy: Multiply):
        self.multiply_strategy = multiply_strategy

    def multiply(self, a: int, b: int):
        return self.multiply_strategy.operate(a, b)


if __name__ == '__main__':
    calculate = Calculate(MultiplyByAddition())
    print(calculate.multiply(5, 4))
