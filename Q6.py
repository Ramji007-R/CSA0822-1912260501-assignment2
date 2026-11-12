
# Q6: Staircase Ways Using Recursion and Memoisation

from functools import lru_cache

# 1. Basic recursive solution
def ways_recursive(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    return ways_recursive(n - 1) + ways_recursive(n - 2)


print("----- Recursive Solution -----")

for n in range(1, 7):
    print("Stairs:", n, "Ways:", ways_recursive(n))


# 2. Call tree for n = 5
print("\n----- Call Tree for n = 5 -----")

print("""
                 ways(5)
                /       \\
           ways(4)     ways(3)
           /    \\       /   \\
       ways(3) ways(2) ways(2) ways(1)
""")

print("Total ways for 5 stairs:", ways_recursive(5))


# 3. Memoisation using lru_cache
memo_calls = 0

@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1

    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


print("\n----- Memoised Solution -----")

for n in range(1, 7):
    ways_memo.cache_clear()
    memo_calls = 0

    result = ways_memo(n)

    print("Stairs:", n, "Ways:", result)


# 4. Compare function calls
print("\n----- Function Call Comparison -----")

for n in [10, 20, 25, 30]:

    # Count calls in normal recursion
    recursive_calls = 0

    def count_recursive(n):
        global recursive_calls
        recursive_calls += 1

        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1

        return count_recursive(n - 1) + count_recursive(n - 2)

    recursive_result = count_recursive(n)

    # Count calls in memoisation
    ways_memo.cache_clear()
    memo_calls = 0

    memo_result = ways_memo(n)

    print("\nStairs:", n)
    print("Ways:", recursive_result)
    print("Normal recursive calls:", recursive_calls)
    print("Memoised calls:", memo_calls)


# 5. Test memoisation for n = 1000
print("\n----- Testing n = 1000 -----")

ways_memo.cache_clear()
memo_calls = 0

try:
    result = ways_memo(1000)
    print("Ways for 1000 stairs:", result)
    print("Memoised calls:", memo_calls)

except RecursionError:
    print("RecursionError: Maximum recursion depth exceeded.")
    print("Memoisation reduces repeated calculations,")
    print("but recursive calls still use the call stack.")


# 6. Iterative alternative
def ways_iterative(n):
    if n < 0:
        return 0

    first = 1
    second = 1

    for i in range(2, n + 1):
        first, second = second, first + second

    return second


print("\n----- Iterative Solution -----")

for n in range(1, 7):
    print("Stairs:", n, "Ways:", ways_iterative(n))

large_result = ways_iterative(1000)

print("Ways for 1000 stairs calculated iteratively.")
print("Number of digits:", len(str(large_result)))
