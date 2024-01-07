def solution(x):
    answer = x % sum([int(i) for i in str(x)]) == 0
    return answer