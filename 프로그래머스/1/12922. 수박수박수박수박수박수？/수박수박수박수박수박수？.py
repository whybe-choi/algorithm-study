def solution(n):
    answer = ''.join(["수" if i % 2 == 0 else "박" for i in range(n)])
    return answer