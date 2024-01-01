def solution(num, total):
    answer = []
    for i in range(-1000, 1000):
        if num * (num - 1 + 2 * i) / 2 == total:
            for _ in range(num):
                answer.append(i)
                i+=1
    return answer