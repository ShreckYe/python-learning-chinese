def fib(N: int) -> int:
    return N if N <= 1 else fib(N - 2) + fib(N - 1)


print([fib(N) for N in range(31)])
