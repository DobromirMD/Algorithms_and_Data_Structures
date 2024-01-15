from datetime import datetime


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_hash(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_hash(n - 1, memo) + fibonacci_hash(n - 2, memo)

    return memo[n]


start_time = datetime.now()
result = fibonacci(40)
end_time = datetime.now()

execution_time = end_time - start_time
print(f"Result: {result}")
print(f"Execution Time: {execution_time.total_seconds()} seconds")

start_time = datetime.now()
result = fibonacci_hash(400)
end_time = datetime.now()
execution_time = end_time - start_time
print(f"Result: {result}")
print(f"Execution Time: {execution_time.total_seconds()} seconds")
