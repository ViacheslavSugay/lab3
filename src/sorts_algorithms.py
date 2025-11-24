from auxiliary_functions import fix_heap

def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    lesser, equal, greater = [], [], []

    for x in arr:
        if x < pivot:
            lesser.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quick_sort(lesser) + equal + quick_sort(greater)


def counting_sort(arr: list[int]) -> list[int]:
    count = [0] * (max(arr) - min(arr) + 1)
    for x in arr:
        count[x - min(arr)] += 1

    result = []
    for i in range(len(count)):
        value = i + min(arr)  # какое это число
        quantity = count[i]  # сколько раз встретилось это число
        for q in range(quantity):
            result.append(value)
    return result


def radix_sort(arr: list[int], base: int = 10) -> list[int]:
    max_digits = max([len(str(x)) for x in arr])
    boxes = [list() for empty in range(base)]

    for i in range(0, max_digits):
        for x in arr:
            digit = (x // base ** i) % base
            target_box = [boxes[i] for i in [digit]][0]
            target_box.append(x)

        new_arr = []
        for line in boxes:
            for x in line:
                new_arr.append(x)
        arr = new_arr

        boxes = [list() for empty in range(base)]
    return arr


def bucket_sort(arr: list[float], buckets: int | None = None) -> list[float]:
    if buckets is None:
        buckets = len(arr)

    buckets_arr = [list() for empty in range(buckets)]

    for num in arr:
        bucket_index = int(num * buckets)
        current_bucket = buckets_arr[bucket_index]
        current_bucket.append(num)

    for bucket in buckets_arr:
        bubble_sort(bucket)
    result = []
    for bucket in buckets_arr:
        for element in bucket:
            result.append(element)

    return result


def heap_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr) // 2 - 1, -1, -1):
        fix_heap(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        fix_heap(arr, i, 0)

    return arr
