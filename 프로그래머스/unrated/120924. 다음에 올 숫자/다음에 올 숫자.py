def solution(common):
    n = len(common) - 1
    if (common[n] - common[n-1]) == (common[n-1] - common[n-2]):
        answer = 2 * common[n] - common[n-1]
    else:
        answer = common[n] ** 2 / common[n-1]
    return answer