import pytest
from src.sorts_algorithms import *
from src.tests_case_generator import *


def test_bubble_sort_random():
    """Тест bubble_sort на случайном массиве"""
    arr = rand_int_array(10, 1, 100)
    result = bubble_sort(arr)
    assert result == sorted(arr)


def test_bubble_sort_nearly_sorted():
    """Тест bubble_sort на почти отсортированном массиве"""
    arr = nearly_sorted(10, 2)
    result = bubble_sort(arr)
    assert result == sorted(arr)


def test_quick_sort_random():
    """Тест quick_sort на случайном массиве"""
    arr = rand_int_array(10, 1, 100)
    result = quick_sort(arr)
    assert result == sorted(arr)


def test_quick_sort_many_duplicates():
    """Тест quick_sort на массиве с дубликатами"""
    arr = many_duplicates(10, 3)
    result = quick_sort(arr)
    assert result == sorted(arr)


def test_counting_sort_random():
    """Тест counting_sort на случайном массиве"""
    arr = rand_int_array(10, 1, 50)
    result = counting_sort(arr)
    assert result == sorted(arr)


def test_counting_sort_reversed():
    """Тест counting_sort на обратно отсортированном массиве"""
    arr = reversed_sorted(10)
    result = counting_sort(arr)
    assert result == sorted(arr)


def test_radix_sort_random():
    """Тест radix_sort на случайном массиве"""
    arr = rand_int_array(10, 1, 100)
    result = radix_sort(arr)
    assert result == sorted(arr)


def test_heap_sort_random():
    """Тест heap_sort на случайном массиве"""
    arr = rand_int_array(10, 1, 100)
    result = heap_sort(arr)
    assert result == sorted(arr)


def test_heap_sort_nearly_sorted():
    """Тест heap_sort на почти отсортированном массиве"""
    arr = nearly_sorted(10, 3)
    result = heap_sort(arr)
    assert result == sorted(arr)


def test_bucket_sort_float():
    """Тест bucket_sort на дробных числах"""
    arr = [0.5, 0.2, 0.9, 0.1, 0.7]
    result = bucket_sort(arr)
    assert result == sorted(arr)


def test_bucket_sort_with_buckets():
    """Тест bucket_sort с указанием количества ведер"""
    arr = [0.3, 0.8, 0.1, 0.6, 0.4]
    result = bucket_sort(arr, 5)
    assert result == sorted(arr)


def test_all_sorts_single():
    """Тест всех сортировок на массиве из одного элемента"""
    single_arr = [5]
    assert bubble_sort(single_arr) == [5]
    assert quick_sort(single_arr) == [5]
    assert counting_sort(single_arr) == [5]
    assert radix_sort(single_arr) == [5]
    assert heap_sort(single_arr) == [5]

    # Для bucket_sort используем float в диапазоне [0, 1)
    assert bucket_sort([0.5]) == [0.5]


def test_all_sorts_duplicates():
    """Тест всех сортировок на массиве с дубликатами"""
    dup_arr = [3, 1, 3, 2, 1]
    sorted_dup = [1, 1, 2, 3, 3]

    assert bubble_sort(dup_arr) == sorted_dup
    assert quick_sort(dup_arr) == sorted_dup
    assert counting_sort(dup_arr) == sorted_dup
    assert radix_sort(dup_arr) == sorted_dup
    assert heap_sort(dup_arr) == sorted_dup

    # Для bucket_sort используем float дубликаты в диапазоне [0, 1)
    dup_float = [0.3, 0.1, 0.3, 0.2, 0.1]
    sorted_dup_float = [0.1, 0.1, 0.2, 0.3, 0.3]
    assert bucket_sort(dup_float) == sorted_dup_float