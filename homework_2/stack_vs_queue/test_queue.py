from queue import Queue
import pytest


def test_queue_operations():
    queue = Queue()
    assert queue.is_empty()
    queue.push(1)
    assert not queue.is_empty()
    assert queue.peek() == 1
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.peek() == 2
    assert queue.pop() == 2
    assert queue.is_empty()


def test_queue_exceptions():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.push(1)
        queue.pop()
        queue.pop()
    with pytest.raises(IndexError):
        queue.push(1)
        queue.push(2)
        queue.pop()
        queue.pop()
        queue.peek()
