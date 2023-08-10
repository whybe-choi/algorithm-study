def solution(my_string):
    result = []
    for i in my_string:
        if i not in result:
            result.append(i)
    answer = ''.join(result)
    return answer