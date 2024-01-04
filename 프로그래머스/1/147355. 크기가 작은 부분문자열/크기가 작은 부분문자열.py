def solution(t, p):
    answer = sum([1 for i in range(len(t)-len(p)+1) if int(t[i:i+len(p)]) <= int(p)])
    return answer