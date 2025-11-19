def quickselect(nums, k):
    k_index = len(nums) - k

    def partition(left, right):
        pivot = nums[right]
        i = left - 1

        for j in range(left, right):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1

    left, right = 0, len(nums) - 1

    while True:
        pivot_index = partition(left, right)

        if pivot_index == k_index:
            return nums[pivot_index]
        elif pivot_index < k_index:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
