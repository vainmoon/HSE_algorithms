def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def sift_up(arr, i):
    while i > 0:
        p = parent(i)
        if arr[p] <= arr[i]:
            break
        arr[p], arr[i] = arr[i], arr[p]
        i = p


def sift_down(arr, n, i):
    while True:
        l = left(i)
        r = right(i)
        smallest = i
        if l < n and arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def makeheap_n_log_n(arr):
    n = len(arr)
    for i in range(1, n):
        sift_up(arr, i)


def makeheap(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        sift_down(arr, n, i)
