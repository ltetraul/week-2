import numpy as np

def ways(n):
    count = 0
    for nickels in range(n // 5 + 1):
        pennies = n - 5 * nickels
        if pennies >= 0:
            count += 1
    return count

#test cases
print(ways(12))
print(ways(20))
print(ways(3))
print(ways(0))
