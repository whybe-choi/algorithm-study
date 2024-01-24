a = int(input())
b = 1000 - a
count = 0

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    count += b//coin
    b %= coin
    
print(count)
    