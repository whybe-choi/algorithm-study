def solution(a, b):
    answer = sum(a[idx]*b[idx] for idx in range(len(a)))
    return answer