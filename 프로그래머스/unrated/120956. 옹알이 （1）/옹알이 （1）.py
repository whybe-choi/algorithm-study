def solution(babbling):
    answer = 0    
    for i in babbling:
        for j in ["aya", "ye", "woo", "ma"]:
            i = i.replace(j, " ")

        if i.isspace() :
            answer += 1
        
    return answer