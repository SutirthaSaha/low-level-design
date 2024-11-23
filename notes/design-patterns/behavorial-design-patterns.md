# Behavioral Design Pattens
## Iterator Pattern
The Iterator Pattern provides a way to access elements of a collection object sequentially without exposing its underlying representation. 
It is a **behavioral design pattern** that allows for the traversal of elements in a collection.
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