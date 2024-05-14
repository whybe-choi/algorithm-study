import sys

def hanoi(a, b, n, moves):
    # 함수 호출 시 k를 1씩 증가
    global k
    k += 1
    # 초기 조건 
    if n == 1:
        moves.append([a, b])
        return 
    # a 장대에서 6-a-b 장대로 n-1개의 원판을 이동
    hanoi(a, 6-a-b, n-1, moves)
    # a 장대에서 b 장대로 n번 원판을 이동
    moves.append([a, b])
    # 6-a-b 장대로 n-1개의 원판을 이동
    hanoi(6-a-b, b, n-1, moves)

n = int(sys.stdin.readline().rstrip())
k = 0
moves = []
hanoi(1, 3, n, moves)

print(k)
for move in moves:
    print(*move)