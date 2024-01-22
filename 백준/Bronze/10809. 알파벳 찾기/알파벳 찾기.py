s = input()

for i in range(ord('a'), ord('z') + 1):
    try:
        print(s.find(chr(i)), end=' ')
    except:
        print(-1, end=' ')