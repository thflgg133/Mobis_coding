import sys

n = int(sys.stdin.readline())

cars = {}
ans = 0

for i in range(n):
    v, w = map(int, sys.stdin.readline().split())
    
    if v not in cars:
        cars[v] = [[w, i+1]] 
        
    else:
        cars[v].append([w, i+1])
              
for i in cars:
    tmp = [0,0]
    
    for j in cars[i]:
        if tmp[0] <= j[0]:
            tmp = j
    
    ans += tmp[1]
    
print(ans)