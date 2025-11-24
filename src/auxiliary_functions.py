def fix_heap(arr, ln, i):
    upper = i
    l, r = 2 * i + 1, 2 * i + 2

    if l < ln and arr[l] > arr[upper]:
        upper = l
    if r < ln and arr[r] > arr[upper]:
        upper = r
    if upper != i:
        arr[i], arr[upper] = arr[upper], arr[i]
        fix_heap(arr, ln, upper)