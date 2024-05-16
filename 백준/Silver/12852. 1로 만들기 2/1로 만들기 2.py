import sys

n = int(sys.stdin.readline().rstrip())

# dp 배열 초기화
dp = [0] * (n + 1)

for i in range(2, n + 1):
    # 현재 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 현재 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 현재 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])

# 연산 과정을 출력
num = n
while num > 1:
    print(num, end=' ')
    # 가장 최적의 경로를 찾아가는 조건문
    if num % 3 == 0 and dp[num] == dp[num // 3] + 1:
        num //= 3
    elif num % 2 == 0 and dp[num] == dp[num // 2] + 1:
        num //= 2
    else:
        num -= 1
print(1)  # 마지막으로 1을 출력
