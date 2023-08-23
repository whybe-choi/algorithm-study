def solution(dots):
    dots = sorted(dots, key=lambda x : x[0])
    answer = abs(dots[1][1] - dots[0][1]) * abs(dots[2][0] - dots[0][0])
    return answer