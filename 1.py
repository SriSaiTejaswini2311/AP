import threading
import time
import random

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def standard_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = standard_merge_sort(arr[:mid])
    right = standard_merge_sort(arr[mid:])
    return merge(left, right)

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = []
    right_part = []

    def sort_left():
        nonlocal left_part
        left_part = parallel_merge_sort(arr[:mid])

    def sort_right():
        nonlocal right_part
        right_part = parallel_merge_sort(arr[mid:])

    left_thread = threading.Thread(target=sort_left)
    right_thread = threading.Thread(target=sort_right)

    left_thread.start()
    right_thread.start()
    left_thread.join()
    right_thread.join()

    return merge(left_part, right_part)

if __name__ == "__main__":
    array = [random.randint(0, 10000) for _ in range(500)]

    start = time.perf_counter()
    standard_merge_sort(array.copy())
    print("Standard Merge Sort Time:", time.perf_counter() - start)

    start = time.perf_counter()
    parallel_merge_sort(array.copy())
    print("Multithreaded Merge Sort Time:", time.perf_counter() - start)
