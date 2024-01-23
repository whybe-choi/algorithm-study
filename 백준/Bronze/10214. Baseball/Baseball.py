t = int(input())

for _ in range(t):
    yonsei_score = []
    korea_score = []
    
    for _ in range(9):
        yonsei, korea = map(int, input().split())
        yonsei_score.append(yonsei)
        korea_score.append(korea)
        
    yonsei_sum = sum(yonsei_score)
    korea_sum = sum(korea_score)
    
    if yonsei_sum > korea_sum:
        print("Yonsei")
    elif yonsei_sum < korea_sum:
        print("Korea")
    else:
        print("Draw")