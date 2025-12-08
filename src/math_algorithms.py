def factorial(n: int) -> int:

    if n < 0:
        raise ValueError('Должно быть неотрицательное число')

    start = 1
    for i in range(1, n + 1):
        start *= i
    return start


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError('Должно быть неотрицательное число')

    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibo(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1

    values = [0, 1]
    while len(values) < n:
        values.append(values[-1] + values[-2])
    return values[-1]


def fibo_recursive(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)