def solution(my_string):
    answer = "".join([i for i in my_string if i not in ['a', 'e', 'i', 'o', 'u']])
    return answer