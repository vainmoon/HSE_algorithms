def merge_sort(arr):
    width = 1
    n = len(arr)
    result = arr[:]

    while width < n:
        for i in range(0, n, 2 * width):
            left = result[i : i + width]
            right = result[i + width : i + 2 * width]
            result[i : i + 2 * width] = merge(left, right)
        width *= 2

    return result


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr):
    a = arr[:]
    stack = [(0, len(a) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot = a[right]
        i = left - 1

        for j in range(left, right):
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[right] = a[right], a[i + 1]
        p = i + 1

        if p - 1 > left:
            stack.append((left, p - 1))
        if p + 1 < right:
            stack.append((p + 1, right))

    return a
