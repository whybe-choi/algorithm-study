def solution(s):
    answer = f"{min(list(map(int, s.split(' '))))} {max(list(map(int, s.split(' '))))}"
    return answer