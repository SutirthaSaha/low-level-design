# Creational Design Patterns
Creational design patterns are a category of design patterns that focus on object creation mechanisms. 
They abstract the instantiation process, making it more flexible and reusable. 

The primary goal of creational patterns is to provide a way to create objects while hiding the creation logic, 
often making the system independent of how its objects are created, composed, and represented.

## Builder Pattern
The Builder Pattern is a creational design pattern that provides a way to construct complex objects step-by-step. 
It separates the construction of a complex object from its representation, allowing the same construction process to 
create different representations. This pattern is particularly useful when an object needs to be created with many 
optional parameters or when the creation process involves multiple steps.

### When to Use
- **Complex Object Construction:** When constructing an object involves multiple steps, and those steps need to be 
executed in a specific order.
- **Optional Parts:** Each part of the house (foundation, structure, roof, interior) is optional. The client can choose 
which parts to build, allowing for partial object creation.
- **Clear and Maintainable Code:** The use of method chaining and clear method names makes the code easy to read and 
maintain by reducing the constructor length.

```python
class House:
    def __init__(self):
        self.foundation: str = "Basic"
        self.structure: str = "Basic walls"
        self.roof: str = "Tiled"
        self.interior: str = "Nothing"
    
    def __str__(self):
        return (
            f"Foundation: {self.foundation}, "
            f"Structure: {self.structure}, "
            f"Roof: {self.roof}, "
            f"Interior: {self.interior}"
        )

class HouseBuilder:
    def __init__(self):
        self.house= House()
    
    def set_foundation(self, foundation: str):
        self.house.foundation = foundation
        return self
    
    def set_structure(self, structure: str):
        self.house.structure = structure
        return self
    
    def set_roof(self, roof: str):
        self.house.roof = roof
        return self

    def get_house(self):
        return self.house

if __name__ == "__main__":
    # Create a basic concrete house with only a concrete foundation and concrete structure  
    basic_house = HouseBuilder().build_foundation("Concrete, brick, and stone").build_structure("Concrete walls")\
        .get_house()  
    print("Basic House:", basic_house)
    
    # Create a fully built house  
    full_house = HouseBuilder().build_foundation("Concrete, brick, and stone")\
        .build_structure("Concrete walls").build_roof("Concrete slab")\
        .build_interior("Wooden furniture").get_house()
    print("Full House:", full_house)  

```

## Prototype Pattern
The Prototype Pattern is a creational design pattern that allows cloning of existing objects without being dependent 
on their concrete classes. 
This pattern is particularly useful when the cost of creating a new instance of a class is more expensive 
than copying an existing one.

## When to Use
- **Performance Optimization:** When creating a new instance of a class is costly (e.g., due to complex initialization, 
database operations, or expensive computations), and you can achieve better performance by copying an existing instance.
- **Simplifying Object Creation:** When the details of the instantiation process are irrelevant to the code that 
needs new instances.
- **Avoiding Subclassing:** When you want to avoid creating a hierarchy of factories or classes just to create objects.

```python
from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum

class ShapeType(Enum):
    CIRCLE = "Circle"
    SQUARE = "Square"

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @abstractmethod
    def clone(self):
        pass
    
    def __str__(self):  
        return f"Shape(x: {self.x}, y: {self.y})"

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def clone(self):
        return Circle(self.x, self.y, self.radius)

class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def clone(self):
        return Square(self.x, self.y, self.side)

class ShapeRegistry:
    def __init__(self):
        self.shapes: Dict[ShapeType,Shape] = {}
    
    def register_shape(self, shape_type: ShapeType, shape: Shape):
        self.shapes[shape_type] = shape
    
    def get_shape(self, shape_type):
        if shape_type not in self.shapes:
            return None
        return self.shapes[shape_type].clone()

if __name__ == "__main__":
    circle = Circle(x=10, y=20, radius=5)
    square = Square(x=20, y=10, side=5)
        
    registry = ShapeRegistry()
    registry.register_shape(circle)
    registry.register_shape(square)

    cloned_circle = registry.get_shape(ShapeType.CIRCLE)
    second_cloned_circle = circle.clone()
    
    print("Original Circle:", circle)  
    print("Cloned Circle:", cloned_circle)
    print("Second Cloned Circle:", second_cloned_circle)
```

## Factory Pattern
The Factory Method Pattern is a design pattern that provides a way to create objects without specifying the exact 
class of the object that will be created. Instead of calling a constructor directly, you call a factory method, 
which creates and returns the object.

### When to Use
- **Exact type of the object is not known until runtime:** The factory design pattern is useful when the creation of 
the object is complex or when you don’t know exactly which class needs to be instantiated.
- **Creation logic is spread across the application:** It helps centralize the creation logic of objects.

```python
from abc import ABC, abstractmethod
from enum import Enum

class Vehicle(ABC):
    def __init__(self, name: str):
        self.name = name
    @abstractmethod
    def drive(self):
        pass

class VehicleType(Enum):
    BIKE = "Bike"
    CAR = "Car"
    TRUCK = "Truck"

class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def drive(self):
        print("Driving a bike")

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def drive(self):
        print("Driving a car")

class VehicleFactory:
    def create(self, name, vehicle_type: VehicleType):
        if vehicle_type == VehicleType.CAR:
            return Car(name)
        elif vehicle_type == VehicleType.BIKE:
            return Bike(name)
        raise Exception("The factory doesn't support production of this vehicle type")

if __name__ == "__main__":
    vehicle_factory = VehicleFactory()
    car = vehicle_factory.create(VehicleType.CAR)
    car.drive()
```
