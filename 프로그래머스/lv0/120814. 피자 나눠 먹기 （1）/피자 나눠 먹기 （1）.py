def solution(n):
    remainer = 1 if n % 7 != 0 else 0
    answer = n // 7 + remainer
    return answer