# Behavioral Design Patterns
Behavioral design patterns are a category of design patterns that focus on the interaction and responsibility 
distribution among objects. They describe patterns of communication between objects and provide solutions to make 
these interactions flexible, efficient, and manageable. 

The primary goal of behavioral design patterns is to encapsulate behavior in such a way that it can be reused and 
extended independent of the objects it operates on.

## Observer Pattern
The Observer Design Pattern is a behavioral design pattern that defines a one-to-many dependency between objects
so that when one object (the subject) changes state, all its dependent objects (observers) are notified
and updated automatically. This pattern is particularly useful in scenarios where multiple objects need to be updated 
in response to a change in another object.

### When to Use
- **State Changes Need to be Propagated:** When a change in one object requires updates in other dependent objects.
- **Decoupling Subjects and Observers:** When you want to promote loose coupling between an object and its dependents.
- **Dynamic Relationships:** When the set of objects that need to be notified can change dynamically.

```python
from abc import ABC, abstractmethod
from typing import List

class Subscriber(ABC):
    @abstractmethod
    def update(self, news: str):
        pass

class EmailSubscriber(Subscriber):
    def update(self, news: str):
        print(f"Email Subscriber: New update - {news}")

class SMSSubscriber(Subscriber):
    def update(self, news: str):
        print(f"SMS Subscriber: New update - {news}")

class NewsAgency:
    def __init__(self):
        self.subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        self.subsribers.append(subscriber)
    
    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)
    
    def notify_subscribers(self, news: str):
        for subscriber in self.subscribers:
            subscriber.update(news)
    
    def add_news(self, news: str):
        print(f"News agency got news: {news}")
        self.notify_subscribers(news)

if __name__ == "__main__":  
    news_agency = NewsAgency()  
  
    email_subscriber = EmailSubscriber()  
    sms_subscriber = SMSSubscriber()
  
    news_agency.subscribe(email_subscriber)  
    news_agency.subscribe(sms_subscriber)
  
    news_agency.add_news("Breaking News: New Observer Pattern Implemented!")  
    news_agency.add_news("Update: Observer Pattern in Python with Analogy")   
```

## State Pattern
The State Design Pattern is a behavioral design pattern that allows an object to alter its behavior when 
its internal state changes. This pattern encapsulates state-specific behavior into separate classes and delegates 
state-related behavior to the current state object. 

### When to Use:
- **Complex and Frequent State Dependent Behavior:** When an object frequently changes states and the state changes are complex, and you want to avoid massive 
conditional statements.
- **State-Specific Behavior:** When different states require different implementations of behavior.
- **Open/Closed Principle:** When you want to add new states without modifying existing code.
- **Clear State Transitions:** When you need clear and explicit state transitions.

```python
from abc import ABC, abstractmethod
class TrafficLightState(ABC):
    @abstractmethod
    def change(self, traffic_light: 'TrafficLight'):
        pass
    @abstractmethod
    def display(self):
        pass

class RedState(TrafficLightState):
    def change(self, traffic_light: 'TrafficLight'):
        traffic_light.state = GreenState()
    def display(self):
        return "Red Light - Stop!"

class YellowState(TrafficLightState):
    def change(self, traffic_light: 'TrafficLight'):
        traffic_light.state = RedState()
    def display(self):
        return "Yellow Light - Slow Down!"

class GreenState(TrafficLightState):
    def change(self, traffic_light: 'TrafficLight'):
        traffic_light.state = YellowState()
    def display(self):
        return "Green Light - Go!"

class TrafficLight:
    def __init__(self):
        self.state: TrafficLightState = RedState()
    def change(self):
        self.state.change()
    def display(self):
        return self.state.display()

if __name__ == "__main__":  
    traffic_light = TrafficLight()  
  
    for _ in range(6):  
        print(traffic_light.display())  
        traffic_light.change_state()
```

## Strategy Pattern
The Strategy Design Pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each 
one of them, and makes them interchangeable. This pattern allows the algorithm to vary independently of the clients 
that use it. It enables selecting an algorithm at runtime.

### When to Use
- **Multiple Algorithms:** When you have multiple algorithms for a specific task, and you want to choose one at runtime.
- **Encapsulation of Algorithms:** When you want to encapsulate the implementation details of the algorithms from the 
clients.
- **Avoid Conditional Statements:** When you want to avoid using conditional statements for selecting different algorithms.
- **Open/Closed Principle:** When you want to adhere to the Open/Closed Principle by allowing new algorithms to be added 
without modifying existing code.

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, nums):
        pass

class MergeSortStrategy(SortStrategy):
    def sort(self, nums):
        print("Sorting using Merge Sort")
        return sorted(nums)

class QuickSortStrategy(SortStrategy):
    def sort(self, nums):
        print("Sorting using Quick Sort")
        return sorted(nums)

class BubbleSortStrategy(SortStrategy):
    def sort(self, nums):
        print("Sorting using Bubble Sort")
        return sorted(nums)

class Sorter:
    def __init__(self, strategy: SortStrategy = QuickSortStrategy()):
        self.strategy = strategy
    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy
    def sort(self, nums):
        return self.strategy.sort(nums)

# client code
if __name__ == '__main__':
    data = [5, 2, 9, 1, 5, 6]
    sorter = Sorter()
    
    # sort data with the initial strategy - Quick Sort
    sorted_data = sorter.sort(data)
    
    # modify the strategy from the client without knowing the internal working
    sorter.set_strategy(MergeSortStrategy())
    sorted_data = sorter.sort(data)
```

## Iterator Pattern
The Iterator Pattern provides a way to access elements of a collection object sequentially without exposing
its underlying representation. It is a **behavioral design pattern** that allows for the traversal of elements 
in a collection.

### When to Use
- **Sequential Access Without Exposing Structure:** When you need to traverse a collection without exposing its underlying 
representation.
- **Custom Traversal Logic:** When you need different ways to traverse a collection, such as forward, backward, or skipping elements.

```python
class ListNode:  
    def __init__(self, val):  
        self.val = val  
        self.next = None  
  
class LinkedList:  
    def __init__(self):  
        self.head = None  
        self.curr = None  
  
    # Method to add a new value to the end of the linked list  
    def add(self, val):  
        node = ListNode(val)  
        if self.head:  
            temp = self.head  
            while temp.next:  
                temp = temp.next  
            temp.next = node  
        else:  
            self.head = node  
  
    # Iterator method to initialize the current node to the head of the list  
    def __iter__(self):  
        self.curr = self.head  
        return self  
  
    # Next method to return the next value in the list and move the current node forward  
    def __next__(self):  
        if self.curr:  
            val = self.curr.val  
            self.curr = self.curr.next  
            return val  
        else:  
            raise StopIteration  
  
    # Generator method to yield values from the linked list one at a time  
    def generate(self):  
        self.curr = self.head  
        while self.curr:  
            val = self.curr.val  
            self.curr = self.curr.next  
            yield val  
  
if __name__ == '__main__':  
    linked_list = LinkedList()  
    linked_list.add(1)  
    linked_list.add(2)  
    linked_list.add(3)  
  
    # Iterator consumption  
    print("Using Iterator:")  
    for value in linked_list:  
        print(value)  
  
    # Generator consumption  
    print("Using Generator:")  
    for value in linked_list.generate():  
        print(value)
```
