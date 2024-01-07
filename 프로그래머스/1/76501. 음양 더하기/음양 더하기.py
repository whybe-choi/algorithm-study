def solution(absolutes, signs):
    answer = sum([absolute if sign else -1 * absolute for absolute, sign in zip(absolutes, signs)])
    return answer