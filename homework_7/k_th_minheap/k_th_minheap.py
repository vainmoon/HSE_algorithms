import heapq


class MinHeap:
    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)
        self._sift_up(len(self.a) - 1)

    def _sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.a[p] <= self.a[i]:
                break
            self.a[p], self.a[i] = self.a[i], self.a[p]
            i = p

    def _sift_down(self, i):
        n = len(self.a)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i
            if l < n and self.a[l] < self.a[smallest]:
                smallest = l
            if r < n and self.a[r] < self.a[smallest]:
                smallest = r
            if smallest == i:
                break
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            i = smallest

    def pop(self):
        last = self.a.pop()
        if not self.a:
            return last
        ret = self.a[0]
        self.a[0] = last
        self._sift_down(0)
        return ret

    def replace_root(self, x):
        if not self.a:
            self.a.append(x)
            return None
        old = self.a[0]
        self.a[0] = x
        self._sift_down(0)
        return old

    def peek(self):
        return self.a[0] if self.a else None

    def __len__(self):
        return len(self.a)


def find_kth_largest_no_heapq(nums, k):
    h = MinHeap()
    for x in nums[:k]:
        h.push(x)
    for x in nums[k:]:
        if x > h.peek():
            h.replace_root(x)
    return h.peek()


def find_kth_largest_with_heapq(nums, k):
    h = []
    for x in nums[:k]:
        heapq.heappush(h, x)
    for x in nums[k:]:
        if x > h[0]:
            heapq.heapreplace(h, x)
    return h[0]
