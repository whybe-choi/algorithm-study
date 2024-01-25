n = int(input())

for _ in range(n):
    p = int(input())
    players = []
    for _ in range(p):
        price, name = input().split()
        players.append([int(price), name])
    print(sorted(players, key=lambda x : (x[0], x[1]), reverse=True)[0][1])