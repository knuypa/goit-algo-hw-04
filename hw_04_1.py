import timeit
import random

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Використання вбудованого в Python сортування Timsort
def timsort(arr):
    return sorted(arr)

# Розміри масивів та параметри для вимірювань часу виконання
array_sizes = [100, 1000, 5000, 10000]
runs = 5
timing_results = {'Insertion Sort': [], 'Merge Sort': [], 'Timsort': []}

# Генерація масивів і вимірювання часу сортування для кожного алгоритму
for size in array_sizes:
    random_array = [random.randint(0, 10000) for _ in range(size)]
    # Сортування вставками
    insertion_time = timeit.timeit('insertion_sort(random_array.copy())', globals=globals(), number=runs)
    timing_results['Insertion Sort'].append(insertion_time)
    # Сортування злиттям
    merge_time = timeit.timeit('merge_sort(random_array.copy())', globals=globals(), number=runs)
    timing_results['Merge Sort'].append(merge_time)
    # Timsort
    timsort_time = timeit.timeit('timsort(random_array.copy())', globals=globals(), number=runs)
    timing_results['Timsort'].append(timsort_time)

# Виведення результатів
print("Порівняльний аналіз продуктивності сортувань:")
for sort_type, times in timing_results.items():
    print(f"\n{sort_type} timings:")
    for size, time in zip(array_sizes, times):
        print(f"Розмір масиву {size}: {time:.5f} секунд")

# Додатковий аналіз середнього часу, якщо потрібно
print("\nДетальний аналіз продуктивності:")
for sort_type in timing_results:
    average_time = sum(timing_results[sort_type]) / len(timing_results[sort_type])
    print(f"Середній час для {sort_type}: {average_time:.5f} секунд")