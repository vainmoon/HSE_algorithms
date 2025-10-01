import sys
import os

sys.path.append(os.getcwd())

from stack_vs_queue.stack import Stack


def validate(pushed, popped):
    stack = Stack()
    popped_idx = 0
    for pushed_idx in range(len(pushed)):
        stack.push(pushed[pushed_idx])

        while not stack.is_empty() and stack.peek() == popped[popped_idx]:
            stack.pop()
            popped_idx += 1

    return stack.is_empty()
