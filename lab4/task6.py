
import time
import statistics

sizes = [10_000, 100_000, 1_000_000]
runs = 7
for size in sizes:
    numbers = list(range(size))
    append_times = []

    for _ in range(runs):
        start = time.time()

        result = []
        for x in numbers:
            if x % 2 == 0:
                result.append(x ** 2)
        end = time.time()
        append_times.append(end - start)
    comprehension_times = []
    for _ in range(runs):
        start = time.time()
        result = [x**2 for x in numbers if x % 2 == 0]
        end = time.time()
        comprehension_times.append(end - start)

    print(f"\nРазмер {size}")
    print("\nappend():")
    for i, t in enumerate(append_times, 1):
        print(f"Запуск {i}: {t:.6f} сек.")
    print(f"Среднее время: {statistics.mean(append_times):.6f} сек.")

    print("\nList comprehension:")
    for i, t in enumerate(comprehension_times, 1):
        print(f"Запуск {i}: {t:.6f} сек.")
    print(f"Среднее время: {statistics.mean(comprehension_times):.6f} сек.")
