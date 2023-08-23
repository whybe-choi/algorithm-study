def solution(numbers):
    answer = max(sorted(numbers)[-1]*sorted(numbers)[-2], sorted(numbers)[0]*sorted(numbers)[1])
    return answer