def solution(num_list):
    odd = 0
    even = 0
    for num in num_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    answer = [even, odd]
    return answer