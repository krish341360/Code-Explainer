# Fibonacci function
def fib(n):
    """
    Computes Fibonacci sequence up to n terms
    Example: fib(5) → [0, 1, 1, 2, 3]
    """
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
