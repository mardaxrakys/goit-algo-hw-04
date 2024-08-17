import timeit
import random


#------------------------------------------------------------------


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
#-------------------------------------------------------------------


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#------------------------------------------------------------------

def time_sorting_algorithm(sort_function, data):
    start_time = timeit.default_timer()
    sort_function(data)
    return timeit.default_timer() - start_time

# Приклад наборів даних
sizes = [100, 1000, 5000, 10000]  # Розміри для тестування
results = { 'merge_sort': [], 'insertion_sort': [], 'timsort': [] }

for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    
    # Вимірювання часу для Merge Sort
    data_copy = data.copy()
    time_taken = time_sorting_algorithm(merge_sort, data_copy)
    results['merge_sort'].append(time_taken)
    
    # Вимірювання часу для Insertion Sort
    data_copy = data.copy()
    time_taken = time_sorting_algorithm(insertion_sort, data_copy)
    results['insertion_sort'].append(time_taken)
    
    # Вимірювання часу для Timsort
    data_copy = data.copy()
    time_taken = time_sorting_algorithm(lambda x: x.sort(), data_copy)
    results['timsort'].append(time_taken)
    
print("Результати:")
for algo, times in results.items():
    print(f"{algo}: {times}")







