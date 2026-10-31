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
    
    print(f"{size} | {t_list_in} | {t_list_out} | {t_set_in} | {t_set_out}")
