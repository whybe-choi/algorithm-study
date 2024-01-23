n = int(input())
vote_cute = []

for i in range(n):
    is_cute = int(input())
    vote_cute.append(is_cute)
   
print("Junhee is cute!" if sum(vote_cute) > n/2 else "Junhee is not cute!")