import sys
import os

sys.path.append(os.getcwd())
from tracer.tracer import tracer_decorator


def get_permutations(nums):
    result = []

    @tracer_decorator
    def forward(current, remaining):
        if not remaining:
            result.append(current)
            return
        for i in range(len(remaining)):
            forward(current + [remaining[i]], remaining[:i] + remaining[i + 1 :])

    forward([], nums)
    return result


if __name__ == "__main__":
    print(get_permutations([0, 1]))
