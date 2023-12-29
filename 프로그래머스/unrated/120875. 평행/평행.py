import numpy as np

def solution(dots):
    first = dots[0]
    second = dots[1]
    third = dots[2]
    fourth = dots[3]
    
    answer = 0
    
    if (first[1] - second[1])/(first[0] - second[0]) == (third[1] - fourth[1])/(third[0] - fourth[0]):
        answer = 1
        
    if (first[1] - third[1])/(first[0] - third[0]) == (second[1] - fourth[1])/(second[0] - fourth[0]):
        answer = 1
    
    if (first[1] - fourth[1])/(first[0] - fourth[0]) == (second[1] - third[1])/(second[0] - third[0]):
        answer = 1

    return answer