import pytest
from src.math_algorithms import *


def test_factorial_basic():
    """Тест факториала на базовых значениях"""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720


def test_factorial_recursive_basic():
    """Тест рекурсивного факториала на базовых значениях"""
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(6) == 720


def test_fibo_basic():
    """Тест чисел Фибоначчи на базовых значениях (нумерация с 1)"""
    assert fibo(1) == 0
    assert fibo(2) == 1
    assert fibo(3) == 1
    assert fibo(4) == 2
    assert fibo(5) == 3
    assert fibo(6) == 5
    assert fibo(7) == 8
    assert fibo(11) == 55


def test_fib_recursive_basic():
    """Тест рекурсивных чисел Фибоначчи на базовых значениях (нумерация с 1)"""
    assert fibo_recursive(1) == 0
    assert fibo_recursive(2) == 1
    assert fibo_recursive(3) == 1
    assert fibo_recursive(4) == 2
    assert fibo_recursive(5) == 3
    assert fibo_recursive(6) == 5
    assert fibo_recursive(7) == 8
    assert fibo_recursive(11) == 55