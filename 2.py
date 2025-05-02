import threading
import time
import random

MAX_ALLOWED_THREADS = 4
active_threads = 0
lock = threading.Lock()

def single_thread_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return single_thread_quicksort(left) + [pivot] + single_thread_quicksort(right)

def threaded_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []

    def sort_left():
        nonlocal left
        left = threaded_quicksort([x for x in arr[1:] if x <= pivot])

    def sort_right():
        nonlocal right
        right = threaded_quicksort([x for x in arr[1:] if x > pivot])

    global active_threads
    with lock:
        can_use_threads = active_threads < MAX_ALLOWED_THREADS
        if can_use_threads:
            active_threads += 2

    if can_use_threads:
        t1 = threading.Thread(target=sort_left)
        t2 = threading.Thread(target=sort_right)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        with lock:
            active_threads -= 2
    else:
        left = threaded_quicksort([x for x in arr[1:] if x <= pivot])
        right = threaded_quicksort([x for x in arr[1:] if x > pivot])

    return left + [pivot] + right

if __name__ == "__main__":
    array = [random.randint(0, 10000) for _ in range(50000)]

    start = time.perf_counter()
    single_thread_quicksort(array.copy())
    print("Single-threaded Quick Sort Time:", time.perf_counter() - start)

    start = time.perf_counter()
    threaded_quicksort(array.copy())
    print("Multithreaded Quick Sort Time:", time.perf_counter() - start)
