import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

# DP table
dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

# 초기값
# 1. 첫번째 글자가 같으면 1 아니면 0
dp[0][0] = 1 if a[0] == b[0] else 0
# 2. b의 첫 글자와 같은 글자가 등장했을 때부터 1
for i in range(1, len(a)):
    dp[i][0] = 1 if b[0] in a[:i+1] else 0
# 3. a의 첫 글자와 같은 글자가 등장했을 때부터 ㅂ
for j in range(len(b)):
    dp[0][j] = 1 if a[0] in b[:j+1] else 0
# DP table 채우기
for i in range(1, len(a)):
    for j in range(1, len(b)):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if a[i] != b[j] else dp[i-1][j-1] + 1

print(dp[len(a)-1][len(b)-1])