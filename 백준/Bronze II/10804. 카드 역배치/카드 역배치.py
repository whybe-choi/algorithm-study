import sys

cards = list(range(1, 21))

for _ in range(10):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    cards = cards[:a-1] + cards[a-1:b][::-1] + cards[b:]

print(*cards, sep=' ')