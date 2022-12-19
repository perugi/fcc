def fib(n):
    if n <= 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# print(fib(5))
# print(fib(6))
# print(fib(7))
# print(fib(50))

print(fib_memo(5))
print(fib_memo(6))
print(fib_memo(7))
print(fib_memo(50))
