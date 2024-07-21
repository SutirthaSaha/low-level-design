class ListNode:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def attach(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def detach_first(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def detach_last(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def detach(self, node):
        if self.head == node:
            self.detach_first()
        elif self.tail == node:
            self.detach_last()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
