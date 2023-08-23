def solution(polynomial):
    terms = polynomial.split(' + ')
    
    const_term = 0
    x_term = 0
    
    for term in terms:
        if 'x' in term:
            coef = term.replace("x", "")
            if coef == '':
                coef = "1"
            x_term += int(coef)
        else:
            const_term += int(term)
            
    result = []
    if x_term != 0:
        if x_term == 1:
            result.append(f"x")
        else:
            result.append(f"{x_term}x")
    
    if const_term != 0:
        result.append(str(const_term))
        
    answer = " + ".join(result)
    return answer