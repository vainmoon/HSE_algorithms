from stack import Stack
import pytest


def test_stack_operations():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()
    assert stack.peek() == 1
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.is_empty()


def test_stack_exceptions():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.push(1)
        stack.pop()
        stack.pop()
    with pytest.raises(IndexError):
        stack.push(1)
        stack.push(2)
        stack.pop()
        stack.pop()
        stack.peek()
