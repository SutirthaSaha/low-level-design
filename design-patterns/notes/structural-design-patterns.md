# Structural Design Patterns
Structural design patterns are a category of design patterns that focus on how classes and objects are composed 
to form larger structures. They ensure that if one part of a system changes, the entire system doesn’t need to change. 

The primary goal of structural patterns is to simplify the design by identifying simple ways to realize relationships 
between entities.

## Adapter Pattern
The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to work together. 
It acts as a bridge between two incompatible interfaces by converting the interface of a class into another interface 
that a client expects.

### When to Use
- Incompatible Interfaces: Use when you need to work with an existing class whose interface is not compatible with the 
rest of your code.
- Third-Party Libraries: Use when integrating third-party libraries or legacy systems that have different interfaces.
- Multiple Implementations: Use when you have multiple classes with different interfaces but need to work with them 
through a unified interface.
- Reuse Without Modification: Use when you want to reuse existing classes without modifying their source code.

```python
from abc import ABC, abstractmethod

# Adaptee Class
class UPI:
    def make_payment(self, amount: float):
        print(f"Processing payment of amount {amount} through UPI")
class Card:
    def pay(self, amount: float):
        print(f"Processing payment of amount {amount} through Card")

# Target Interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Adapter Class
class UPIAdapter(PaymentProcessor):
    def __init__(self, upi: UPI):
        self.upi = upi
    
    def process_payment(self, amount):
        self.upi.make_payment(amount)

class CardAdapter(PaymentProcessor):
    def __init__(self, card: Card):
        self.card = card
    
    def process_payment(self, amount):
        self.card.pay(amount)

# client code
if __name__ == "__main__":
    upi = UPI()
    upi_adapter = UPIAdapter(upi)

    card = Card()
    card_adapter = CardAdapter(card)

    upi_adapter.process_payment(100)
    card_adapter.process_payment(20)
```

## Proxy Pattern
The Proxy Pattern is a structural design pattern that provides a surrogate or placeholder for another object to 
control access to it. The proxy can perform additional operations like logging, access control, 
or caching when the actual object is accessed.

### When to Use
- **Lazy Initialization:** Use when you want to delay the creation and initialization of the actual object until it’s needed.
- **Access Control:** Use when you need to control access to the object, for example, when different users should have 
different levels of access.
- **Logging and Monitoring:** Use when you need to add logging, monitoring, or other similar functionality without 
modifying the actual object.
- **Remote Access:** Use when the object resides in a different address space, such as in a different machine or a 
different process.

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def query(self, sql: str):
        pass

class RealDatabase(Database):
    def query(self, sql: str):
        print(f"Executing query: {sql}")

# Proxy Class - to control access and additional logging
class DatabaseProxy:
    def __init__(self):
        self.database = RealDatabase()
    
    def query(self, sql: str):
        print(f"Logging: About to execute query: {sql}")
        self.database.query(sql)

if __name__ == "__main__":
    db_proxy = DatabaseProxy()
    db_proxy.query("SELECT * from USERS")
```

## Facade Pattern
The Facade Pattern is a structural design pattern that provides a simplified interface to a complex subsystem. 
It defines a higher-level interface that makes the subsystem easier to use.

### When to Use
- **Complex Subsystems:** Use when you have a complex subsystem with many interfaces, and you want to simplify 
its usage.
- **Legacy Systems:** Use when integrating with a legacy system to provide a more straightforward interface.
- **Unified Interface:** Use when you need to provide a unified interface to a set of interfaces in a subsystem 
to make it easier to use.

```python
# Subsystem Classes
class CPU:
    def start(self):
        print("CPU started")
class Memory():
    def load(self):
        print("Memory loaded")
class HardDrive:
    def read(self):
        print("Hard drive read")

# Facade Class
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start(self):
        print("Starting computer...")
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()
        print("Computer started")    

# Client Code
if __name__ == "__main__":
    computer = Computer()
    computer.start()
```
