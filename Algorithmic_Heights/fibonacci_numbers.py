#
# Fibonacci Numbers
#
# Given: A positive integer n <= 25
# Return: The value of Fn
#


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


N = 6
print(fibonacci(N))
