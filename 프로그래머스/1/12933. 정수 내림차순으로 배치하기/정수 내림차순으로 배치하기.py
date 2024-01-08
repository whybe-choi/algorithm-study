def solution(n):
    answer = int(''.join(map(str, sorted([int(i) for i in str(n)], reverse=True))))
    return answer