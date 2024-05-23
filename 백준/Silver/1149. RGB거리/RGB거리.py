import sys

n = int(sys.stdin.readline().rstrip())
# 0 - R / 1 - G / 2 - B
cost = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# DP 테이블 선언
# DP[i][j] : i번째 집이 j색일 때 집을 칠하는 최소비용
dp = [[0]*3 for _ in range(n)]
# 초기값
# 첫번째 집의 경우에는 단순히 해당 집을 각 색으로 칠하는 비용이 최소비용이 된다.
for color in range(3):
    dp[0][color] = cost[0][color]
# DP 테이블 채우기
for i in range(1, n):
    # i번째 집을 빨강으로 칠할 경우
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    # i번째 집을 초록으로 칠할 경우
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    # i번째 집을 파랑으로 칠할 경우
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n-1]))