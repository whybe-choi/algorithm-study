for _ in range(int(input())):
    r, s = input().split()
    print(''.join([string * int(r) for string in list(s)]))