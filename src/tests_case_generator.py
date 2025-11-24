import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    return [random.randint(lo, hi) for el in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    arr = [el for el in range(n)]

    for i in range(swaps):
        el1, el2 = random.randint(i, n - 1), random.randint(i, n - 1)
        arr[el1], arr[el2] = arr[el2], arr[el1]

    return arr


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    unique_arr = [el for el in range(k_unique)]
    many_duplicates_arr = [random.choice(unique_arr) for i in range(n)]

    return many_duplicates_arr


def reversed_sorted(n: int, *, seed=None) -> list[int]:
    arr = [el for el in range(n)]

    return arr[::-1]


def rand_float_array(n: int, lo: int, hi: int, *, seed=None) -> list[float]:
    return [random.randint(lo, hi) for i in range(n)]
