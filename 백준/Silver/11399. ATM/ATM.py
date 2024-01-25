n = int(input())
minutes = list(map(int, input().split()))

cumsum_list = []
cumsum = 0

for minute in sorted(minutes):
    cumsum += minute
    cumsum_list.append(cumsum)
    
print(sum(cumsum_list))
