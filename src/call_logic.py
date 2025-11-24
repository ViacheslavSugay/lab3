from math_algorithms import *
from sorts_algorithms import *
from data_structures import *

alg = {'math': {"factorial": factorial, "factorial_recursive": factorial_recursive, "fibo": fibo,
                "fibo_recursive": fibo_recursive},

       'sorts': {"bubble": bubble_sort, "quick": quick_sort, "counting": counting_sort, "radix": radix_sort,
                 "bucket": bucket_sort, "heap": heap_sort}}
s = [""]

structures = {
    'stack': Stack(),
    'queue': Queue()
}


def pars(n: str):
    n = n.split(' ', 2)

    if n[0] == 'math':
        if n[1] not in alg['math']:
            raise SyntaxError(f'{n[1]}: такой математической функции нет!')
        return alg[n[0]][n[1]](int(n[2]))

    if n[0] == 'sorts':
        func_name = n[1].split('=')[0]

        if func_name not in alg['sorts']:
            raise SyntaxError(f'{func_name}: такой сортировки нет!')

        if func_name == 'bucket':
            if '=' in n[1]:
                buckets_count = n[1].split('=')[1]
                buckets = int(buckets_count)
            else:
                buckets = None

            digit_arr = list(map(float, ((n[2][1:-1]).split(', '))))
            f = alg[n[0]][func_name](digit_arr, buckets)

        elif func_name in ['bubble', 'quick', 'counting', 'radix', 'heap']:
            digit_arr = list(map(int, ((n[2][1:-1]).split(', '))))
            f = alg[n[0]][func_name](digit_arr)

        return f

    if n[0] == "stack" or n[0] == "queue":
        if len(n) < 2:
            raise SyntaxError("Недостаточно аргументов! Формат: структура метод [значение]")

        struct_type = n[0]
        method = n[1]

        if struct_type not in structures:
            raise SyntaxError(f"{struct_type}: такой структуры нет! Доступные: stack, queue")

        struct = structures[struct_type]

        if method == 'push' or method == 'enqueue':
            if len(n) < 3:
                raise SyntaxError(f"Метод {method} требует значение!")
            value = int(n[2])

            if method == 'push':
                struct.push(value)
            else:
                struct.enqueue(value)
            f = f"Добавлено: {value}"

        elif method == 'pop':
            f = f"Извлечено: {struct.pop()}"

        elif method == 'dequeue':
            f = f"Извлечено: {struct.dequeue()}"

        elif method == 'peek':
            f = f"Верхний элемент: {struct.peek()}"

        elif method == 'front':
            f = f"Первый элемент: {struct.front()}"

        elif method == 'is_empty':
            f = f"Пустая: {struct.is_empty()}"

        elif method == 'len':
            f = f"Размер: {len(struct)}"

        elif method == 'min':
            f = f"Минимальный: {struct.min()}"

        elif method == 'show':
            f = f"Содержимое: {struct.items}"

        else:
            raise SyntaxError(f"{method}: такого метода нет!")

        return f

    else:
        raise SyntaxError(f'{n[0]}: такого типа функций или структуры нет!')