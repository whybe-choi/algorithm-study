def solution(M, N):
    if (M * N // 2) != 0:
        answer = M * N - 1
    else:
        answer = 0
    return answer