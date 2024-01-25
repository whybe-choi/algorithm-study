n = int(input())
score = list(map(int, input().split()))
m = max(score)

print(f"{sum(score)/m * 100 / n}")