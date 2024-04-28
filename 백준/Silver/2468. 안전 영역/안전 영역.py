import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
area = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]  #입력받기

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def dfs(x,y,h):       #범위내 조건을 만족하면 재귀 돌면서 실행
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0<=nx<N) and (0<=ny<N) and (area[nx][ny]>h) and not(visited[nx][ny]):
      visited[nx][ny] = True
      dfs(nx,ny,h)

ans = 1
for i in range(101):        #높이비교
  visited = [[False]*N for _ in range(N)]
  cnt = 0
  for j in range(N):
    for k in range(N):
      if (area[j][k]>i) and not(visited[j][k]):   #비가 온거보다 높고 방문하지 않았으면
        cnt += 1
        visited[j][k] = True
        dfs(j,k,i)
  ans = max(ans, cnt)
print(ans)