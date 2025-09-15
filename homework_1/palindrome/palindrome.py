def check_for_palindrome(num: int) -> bool:
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num <= 0:
        raise ValueError("Input must be a positive number")

    inverted_num = 0
    tmp_num = num
    while tmp_num:
        inverted_num += tmp_num % 10
        inverted_num *= 10
        tmp_num //= 10

    inverted_num //= 10
    return inverted_num == num
