
# Q7: Diagnose, Redesign and Validate
# Selected Program: Staircase Ways (Q6)

import time
import sys

# ------------------------------------------------
# 1. ORIGINAL SOLUTION - NORMAL RECURSION
# ------------------------------------------------

recursive_calls = 0

def ways_recursive(n):
    global recursive_calls
    recursive_calls += 1

    if n <= 1:
        return 1

    return ways_recursive(n - 1) + ways_recursive(n - 2)


# ------------------------------------------------
# 2. REDESIGNED SOLUTION - MEMOISATION
# ------------------------------------------------

memo_calls = 0

def ways_memo(n, cache=None):
    global memo_calls

    if cache is None:
        cache = {}

    memo_calls += 1

    if n <= 1:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = ways_memo(n - 1, cache) + ways_memo(n - 2, cache)

    return cache[n]


# ------------------------------------------------
# 3. ITERATIVE SOLUTION - LAST TWO VALUES
# ------------------------------------------------

iterative_steps = 0

def ways_iterative(n):
    global iterative_steps
    iterative_steps = 0

    if n <= 1:
        return 1

    first = 1
    second = 1

    for i in range(2, n + 1):
        first, second = second, first + second
        iterative_steps += 1

    return second


# ------------------------------------------------
# 4. COMPARE ALL THREE METHODS
# ------------------------------------------------

print("Q7: STAIRCASE WAYS - PERFORMANCE COMPARISON")
print("=" * 55)

test_values = [10, 20, 25]

for n in test_values:

    # Original recursion
    recursive_calls = 0

    start = time.perf_counter()
    result1 = ways_recursive(n)
    recursive_time = time.perf_counter() - start

    # Memoisation
    memo_calls = 0

    start = time.perf_counter()
    result2 = ways_memo(n)
    memo_time = time.perf_counter() - start

    # Iterative method
    start = time.perf_counter()
    result3 = ways_iterative(n)
    iterative_time = time.perf_counter() - start

    print("\nNumber of stairs:", n)
    print("Results match:", result1 == result2 == result3)
    print("Number of ways:", result1)

    print("\nNormal Recursion:")
    print("Function calls:", recursive_calls)
    print("Execution time:", recursive_time)

    print("\nMemoisation:")
    print("Function calls:", memo_calls)
    print("Execution time:", memo_time)

    print("\nIterative Method:")
    print("Loop iterations:", iterative_steps)
    print("Execution time:", iterative_time)


# ------------------------------------------------
# 5. TEST LARGE INPUT - n = 1000
# ------------------------------------------------

print("\n" + "=" * 55)
print("LARGE INPUT TEST")

large_n = 1000

print("Number of stairs:", large_n)

start = time.perf_counter()
large_result = ways_iterative(large_n)
large_time = time.perf_counter() - start

print("Iterative calculation completed successfully.")
print("Number of digits in result:", len(str(large_result)))
print("Execution time:", large_time, "seconds")

print("\nPython recursion limit:", sys.getrecursionlimit())

print("\nConclusion:")
print("Memoisation avoids repeated recursive calculations.")
print("The iterative method avoids recursive call-stack limits.")
