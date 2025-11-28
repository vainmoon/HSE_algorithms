import random
import time
from makeheap import makeheap, makeheap_n_log_n


def time_func(fn, arr):
    start = time.perf_counter()
    fn(arr)
    end = time.perf_counter()
    return end - start


def run_bench(sizes, trials):
    print("n, avg_time_makeheap (s), avg_time_makeheap_n_log_n (s)")
    for n in sizes:
        t1 = 0.0
        t2 = 0.0
        for _ in range(trials):
            arr = [random.randint(0, 10**6) for _ in range(n)]
            a = arr.copy()
            b = arr.copy()
            t1 += time_func(makeheap, a)
            t2 += time_func(makeheap_n_log_n, b)
        print(f"{n}, {t1 / trials:.6f}, {t2 / trials:.6f}")


if __name__ == "__main__":
    run_bench([100, 1000, 5000, 10000, 100000], 100)
