def solution(genres, plays):
    best = {}
    total_playing = []
    answer = []
    
    for idx, genre, play in zip(range(len(genres)), genres, plays):
        if genre not in best.keys():
            best[genre] = [(idx, play)]
        else:
            best[genre].append((idx, play))
    
    for key in best.keys():
        best[key] = sorted(best[key], key=lambda x : x[1], reverse=True)

    for key, value in best.items():
        playing = sum([play[1] for play in value])
        total_playing.append((key, playing))
    
    total_playing = sorted(total_playing, key=lambda x : x[1], reverse=True)
        
    print(best)
    print(total_playing)
    
    for genre, _ in total_playing:
        count = 0
        for idx, play in best[genre]:
            if count == 2:
                break
            answer.append(idx)
            count += 1
    
    return answer