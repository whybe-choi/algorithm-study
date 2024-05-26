import sys

n = int(sys.stdin.readline().rstrip())

meeting = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 회의를 끝나는 시간이 빠른 순으로, 끝나는 시간이 같다면 시작 시간이 빠른 순으로 정렬
meeting.sort(key=lambda x:(x[1], x[0]))

# 끝나는 시간이 현재 기준으로 빠른 회의부터 계속 선택하면 최대 사용할 수 있는 회의의 최대 개수가 됨
# 정렬된 회의의 첫번째 회의를 우선 선택
end = meeting[0][1]
count = 1
for i in range(1, n):
    # 현재 회의가 끝나는 시간 이후에 진행 가능한 회의 중 가장 빠른 회의를 진행
    if end <= meeting[i][0]:
        end = meeting[i][1]
        count += 1

print(count)