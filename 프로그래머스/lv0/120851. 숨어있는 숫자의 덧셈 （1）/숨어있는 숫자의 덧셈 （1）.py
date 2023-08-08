import re

def solution(my_string):
    result = re.sub("[a-zA-Z]", '', my_string)
    answer = sum([int(i) for i in result])
    return answer