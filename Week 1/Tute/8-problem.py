# Write code that calculates the fibonacci numbers iteratively.
# F(1) == F(2) == 1
def fibIter(x):
    seq = [1, 1]
    # Return fib(x) immediately if already calculated.
    if (x <= len(seq)):
        return 1
    for i in range(1, x-1):
        seq.append(seq[i]+ seq[i-1])
    return seq[-1]

"""
Time complexity:
    O(n)
Space complexity:
    O(1)
"""

# Write code that calculates the fibonacci numbers recursively.
def fibRec(x):
    if (x == 0):
        return 0
    elif (x == 1):
        return 1
    else:
        return fibRec(x-1) + fibRec(x-2)

"""
Time complexity:
    O(2^n)
Space complexity:
    O(n)
"""