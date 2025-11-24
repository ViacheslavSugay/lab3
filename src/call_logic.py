from math_algorithms import *
from sorts_algorithms import *
from tests_case_generator import *

alg = {'math': {"factorial": factorial, "factorial_recursive": factorial_recursive, "fibo": fibo,
                "fibo_recursive": fibo_recursive},

       'sorts': {"bubble": bubble_sort, "quick": quick_sort, "counting": counting_sort, "radix": radix_sort,
                 "bucket": bucket_sort, "heap": heap_sort},

       'tests': {"rand_int": rand_int_array, "nearly": nearly_sorted, "many_duplicates": many_duplicates,
                 "reversed": reversed_sorted}}


def pars(n: str):
    n = n.split(' ', 2)

    if n[0] == 'math':
        if n[1] not in alg['math']:
            raise SyntaxError(f'{n[1]}: такой математичсекой функции нет!')
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
    else:
        raise SyntaxError(f'{n[0]}: такого типа функций нет!')