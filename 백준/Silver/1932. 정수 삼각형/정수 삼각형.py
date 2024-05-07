import sys

n = int(sys.stdin.readline().rstrip())

triangle = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

# 초기값
dp[0][0] = triangle[0][0]

# 가장 왼쪽 열
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + triangle[i][0]

# 대각선
for i in range(1, n):
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]

# DP 테이블 채우기
for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

print(max(dp[n-1]))