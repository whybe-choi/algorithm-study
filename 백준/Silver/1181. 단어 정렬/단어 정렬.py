import sys

n = int(sys.stdin.readline().rstrip())

words = set()
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.add(word)
    
for word in sorted(list(words), key=lambda x : (len(x), x)):
    print(word)