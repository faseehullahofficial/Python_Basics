# Recursion: When a function calls itself repeadetly


# Example 1 | Count Down using if statement

def CountD(n):
    if (n == 0):
        return
    print(n)
    CountD(n-1)


CountD(5)

# Example 2 | Calculation Sum of CountD()


def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n


sum = calc_sum(5)
print(sum)

# Example 3 | Factorial Function


def factorial_loop(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example usage
print(factorial_loop(5))  # Output: 120
