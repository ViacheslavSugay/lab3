import time
from typing import Dict, List, Callable
from arr import *
from sorts_algorithms import *

def timeit_once(func: Callable, *args, **kwargs) -> float:
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start

def benchmark_sorts(arrays: Dict[str, List], algos: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    result = {
        alg_name: {
            arr_name: timeit_once(alg_func, arr.copy())
            for arr_name, arr in arrays.items()
        }
        for alg_name, alg_func in algos.items()
    }
    return result


def print_results(results):
    output = "БЕНЧМАРК СОРТИРОВОК:\n"

    for alg_name, alg_results in results.items():
        output += f"\n{alg_name}:\n"
        for arr_name, time_taken in alg_results.items():
            output += f"  {arr_name}: {time_taken:.6f} сек\n"

    return output