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

def ways(cents, coin_types=[1, 5]):
    #dynamic approach
    dp = [0] * (cents + 1)
    dp[0] = 1
    for coin in coin_types:
        for i in range(coin, cents + 1):
            dp[i] += dp[i - coin]
    return dp[cents]

#test cases
print(ways(12))           
print(ways(20))           
print(ways(3))            
print(ways(0))             
print(ways(100, [25, 10, 5, 1]))

def lowest_score(names, scores):
    return names[np.argmin(scores)]

def sort_names(names, scores):
    return names[np.argsort(scores)[::-1]]

scores = np.array([99, 71, 85, 62, 91])
names = np.array(['Lucas', 'Ethan', 'Peter', 'Tyler', 'Cobey'])

print("Lowest score:", lowest_score(names, scores))
print("Names sorted by score:", sort_names(names, scores))
