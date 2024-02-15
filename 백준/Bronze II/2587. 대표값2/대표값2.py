import sys

scores = []

for _ in range(5):
    score = int(sys.stdin.readline().rstrip())
    scores.append(score)
    
print(int(sum(scores)/5))
print(sorted(scores)[2])