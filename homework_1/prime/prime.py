def count_prime(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive.")

    if n <= 2:
        return 0

    sieve = [False, False] + [True] * (n - 2)
    sieve_num = 1
    while sieve_num**2 < n:
        sieve_num += 1
        if not sieve[sieve_num]:
            continue
        for i in range(sieve_num**2, n, sieve_num):
            sieve[i] = False
    return sum(sieve)
