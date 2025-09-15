def get_max_even_sum(array: list) -> int:
    if not array:
        raise ValueError("The array must not be empty.")

    sum = 0
    min_odd_num = float("inf")
    for num in array:
        if num % 2 != 0 and num < min_odd_num:
            min_odd_num = num
        sum += num

    return sum if sum % 2 == 0 else sum - min_odd_num
