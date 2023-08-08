import re

def solution(my_string):
    
    answer = sorted([int(i) for i in re.sub('[a-z]', '', my_string)])
    return answer