def get_solution(arr, k):
    remainder_dict = {}
    for i, num in enumerate(arr):
        if num in remainder_dict:
            return remainder_dict[num], i
        remainder_dict[k - num] = i
    return None
