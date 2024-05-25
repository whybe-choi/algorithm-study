import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# 필요한 동전 개수
answer = 0
# 마지막 동전부터 시작해서
for i in range(n-1, -1, -1):
    # K를 해당 동전으로 나눈 몫은 곧 동전 개수를 의미함
    answer += (k // coins[i])
    # K를 해당 동전으로 나눈 나머지는 해당 동전을 사용하고 남은 가치를 의미함
    k %= coins[i]
print(answer)