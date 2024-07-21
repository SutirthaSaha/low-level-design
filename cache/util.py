class ListNode:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.node_map = dict()

    def add(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.node_map[val] = node

    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove_first(self):
        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return node

    def remove_last(self):
        node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return node

    def remove_val(self, val) -> ListNode:
        if self.head.val == val:
            return self.remove_first()
        elif self.tail.val == val:
            return self.remove_last()
        else:
            node = self.node_map[val]
            node.prev.next = node.next
            node.next.prev = node.prev
            return node
