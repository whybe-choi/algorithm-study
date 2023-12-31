def solution(id_pw, db):
    ids = [info[0] for info in db]
    pws = [info[1] for info in db]
    
    if id_pw in db:
        answer = 'login'
    elif id_pw[0] not in ids:
        answer = 'fail'
    else:
        answer = 'wrong pw'
        
    return answer
            