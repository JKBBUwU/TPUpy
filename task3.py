import timeit

sizes = [100, 10_000, 1_000_000]

for size in sizes:
    data_list = list(range(size))
    data_set = set(data_list)
    
    val_present = size // 2
    val_missing = size + 1
    
    runs = 10000 if size < 1_000_000 else 100
    
    t_list_in = timeit.timeit(lambda: val_present in data_list, number=runs) / runs * 1e9
    t_list_out = timeit.timeit(lambda: val_missing in data_list, number=runs) / runs * 1e9
    t_set_in = timeit.timeit(lambda: val_present in data_set, number=runs) / runs * 1e9
    t_set_out = timeit.timeit(lambda: val_missing in data_set, number=runs) / runs * 1e9
    
    print(f"{size:<10,} | {t_list_in:<15.1f} | {t_list_out:<15.1f} | {t_set_in:<18.1f} | {t_set_out:<18.1f}")
