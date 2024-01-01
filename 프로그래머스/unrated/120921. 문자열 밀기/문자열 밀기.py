def solution(A, B):
    answer = 0
    i = 1
    C = A
    while C != B:
        if i == len(A):
            return -1
        C = A[len(A)-i:] + A[:len(A)-i]
        answer += 1
        i += 1
    return answer