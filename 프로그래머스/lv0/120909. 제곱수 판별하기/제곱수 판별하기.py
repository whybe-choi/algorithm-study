import math

def solution(n):
    answer = 1 if math.sqrt(n).is_integer() else 2
    return answer