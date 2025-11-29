from tests_case_generator import *
from sorts_algorithms import *

arrays = {
    "random_100": rand_int_array(100, 0, 100),
    "random_500": rand_int_array(500, 0, 500),
    "nearly_sorted_100": nearly_sorted(100, 10),
    "nearly_sorted_500": nearly_sorted(500, 50),
    "many_duplicates_100": many_duplicates(100, 5),
    "many_duplicates_500": many_duplicates(500, 10),
    "reversed_100": reversed_sorted(100),
    "reversed_500": reversed_sorted(500)
}

algos = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "counting_sort": counting_sort,
    "radix_sort": radix_sort,
    "heap_sort": heap_sort
}