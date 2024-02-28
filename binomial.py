def factorial(n):
    if (n >= 1):
        return n * factorial(n - 1)
    elif (n == 0):
        return 1
    else: # n < 0
        raise ArithmeticError("Well, non-negative integers only.")

# Computes the binomial coefficient of n over k; parameters n and k are integers. Returns
# the value n over k as an integer (because it always must be
# an integer).
def binomialCoefficient (n, k):
    if k > n:
        return 0
    return int(factorial(n)/(factorial(k) * factorial(n - k)))