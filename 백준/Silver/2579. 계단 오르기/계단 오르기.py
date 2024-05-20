import sys

n = int(sys.stdin.readline().rstrip())
scores = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

if n == 1:
    print(scores[0])
elif n == 2:
    print(scores[0] + scores[1])
else:
    dp = [[0 for _ in range(2)] for _ in range(n)]
    # 첫번째 계단으로 바로 오르는 경우
    dp[0][0] = scores[0]
    # 두번째 계단으로 바로 오르는 경우
    dp[1][0] = scores[1]
    # 첫번째 계단에서 두번째 계단으로 오르는 경우
    dp[1][1] = scores[0] + scores[1]

    for i in range(2, n):
        for j in range(2):
            if j == 0:
                dp[i][j] = max(dp[i-2]) + scores[i]
            else:
                dp[i][j] = dp[i-1][0] + scores[i]

    print(max(dp[n-1]))