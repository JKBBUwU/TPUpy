import sys
bo = {}
bo[1] = "asdasdasdasdasdasdasda"
print(bo[1])

N = 10_000


test_tuple = tuple(range(N))
test_list  = list(range(N))
test_set   = set(range(N))
test_dict  = {i: f"val_{i}" for i in range(N)}


print("")
print(f"{sys.getsizeof(test_tuple)}")
print(f"{sys.getsizeof(test_list)}")
print(f"{sys.getsizeof(test_set)}")
print(f"{sys.getsizeof(test_dict)}")
