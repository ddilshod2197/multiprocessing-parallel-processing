import multiprocessing
import time

def parallel_map(func, iterable):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(func, iterable)
    pool.close()
    pool.join()
    return results

def square(x):
    return x ** 2

if __name__ == "__main__":
    numbers = [i for i in range(1000000)]
    start_time = time.time()
    results = parallel_map(square, numbers)
    end_time = time.time()
    print(f"Natija: {results[:10]}")
    print(f"Vaqt: {end_time - start_time} soniya")
```

```python
import multiprocessing
import time

def parallel_map(func, iterable):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(func, iterable)
    pool.close()
    pool.join()
    return results

def square(x):
    return x ** 2

if __name__ == "__main__":
    numbers = [i for i in range(1000000)]
    start_time = time.time()
    results = parallel_map(square, numbers)
    end_time = time.time()
    print(f"Natija: {results[:10]}")
    print(f"Vaqt: {end_time - start_time} soniya")
