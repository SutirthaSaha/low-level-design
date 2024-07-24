class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.curr = None

    def add(self, val):
        node = ListNode(val)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            self.head = node

    # iterator
    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if self.curr:
            val = self.curr.val
            self.curr = self.curr.next
            return val
        else:
            raise StopIteration

    # generator
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

    # iterator
    for val in linked_list:
        print(val)

    # generator
    for val in linked_list.generate():
        print(val)
