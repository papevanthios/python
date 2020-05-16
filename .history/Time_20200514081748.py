from HeaderFiles import Header1
import timeit
for _ in range(10)

    print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
    print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
