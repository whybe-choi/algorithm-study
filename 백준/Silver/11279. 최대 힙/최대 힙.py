from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(n):
    x = int(int(sys.stdin.readline().rstrip()))
    if x == 0:
        print(-1 * heappop(heap) if len(heap) != 0 else 0)
    else:
        heappush(heap, -1 * x)