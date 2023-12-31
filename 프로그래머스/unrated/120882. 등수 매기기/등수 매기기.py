def solution(score):
    avg = [sum(i) / 2 for i in score]
    sorted_avg = sorted(avg, reverse=True)
    answer = [sorted_avg.index(i)+1 for i in avg]
    return answer