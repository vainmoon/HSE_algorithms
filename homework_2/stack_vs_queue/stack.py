class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        self.top = ListNode(value, self.top)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        pop_value = self.top.value
        self.top = self.top.next
        return pop_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.top.value
