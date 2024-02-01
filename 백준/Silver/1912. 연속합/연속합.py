import sys

# 정수 n과 n개의 정수로 이루어진 수열
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

# i열의 최댓값을 저장하기 위한 DP 테이블
dp = [0] * n

dp[0] = nums[0]

for i in range(1, n):
	# 이전 열의 최댓값에 현재 열의 대각선의 숫자를 더한 값과 현재 열의 대각선의 숫자를 비교
	if dp[i-1] + nums[i] > nums[i]:
		dp[i] = dp[i-1] + nums[i]
	else:
		dp[i] = nums[i]

print(max(dp))