def solution(rsp):
    counterpart = {"2" : "0", "0" : "5", "5" : "2"}
    answer = "".join([counterpart[i] for i in rsp])
    return answer