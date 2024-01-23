while True:
    n = int(input())
    
    if n == -1:
        break
        
    divisor = [i for i in range(1, n) if n % i == 0]
    
    if n == sum(divisor):
        print(f"{n} = {' + '.join(map(str, divisor))}")            
    else:
        print(f"{n} is NOT perfect.")
    
    
            