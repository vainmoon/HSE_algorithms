class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None

    def is_empty(self):
        return self.bottom is None

    def push(self, value):
        if self.bottom is None:
            self.bottom = ListNode(value)
            self.top = self.bottom
            return

        self.top.next = ListNode(value)
        self.top = self.top.next

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        pop_value = self.bottom.value
        self.bottom = self.bottom.next
        return pop_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.bottom.value
