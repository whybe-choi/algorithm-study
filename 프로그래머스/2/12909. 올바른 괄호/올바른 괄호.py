def solution(s):
    stack = []
    
    for i in s:
        if i == "(": 
            stack.append("(")
        elif i == ")": 
            try:
                stack.pop()
            except:
                answer = False
                return answer
        
    if len(stack) == 0:
        answer = True
    else:
        answer = False
        
    return answer