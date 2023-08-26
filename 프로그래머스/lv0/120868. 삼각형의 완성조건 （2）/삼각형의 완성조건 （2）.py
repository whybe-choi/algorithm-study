def solution(sides):
    a, b = sorted(sides)
    case1 = a
    case2 = a - 1
    answer = case1 + case2
    return answer