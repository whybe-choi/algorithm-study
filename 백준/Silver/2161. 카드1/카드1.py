from collections import deque

n = int(input())
cards = deque([i for i in range(n, 0, -1)])
# 버린 카드들을 추가할 리스트
results = []

while len(cards) != 0:
    # 제일 위에 있는 카드를 바닥에 버린다.
    results.append(cards.pop())
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    cards.rotate()

print(' '.join(map(str, results)))
