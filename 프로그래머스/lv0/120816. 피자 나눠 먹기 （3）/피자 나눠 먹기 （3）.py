def solution(slice, n):
    remainer = 1 if n % slice != 0 else 0
    answer = n // slice + remainer
    return answer