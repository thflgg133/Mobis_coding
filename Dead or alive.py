import sys

n = int(sys.stdin.readline())

cars = {}
ans = 0

for i in range(n):
    v, w = map(int, sys.stdin.readline().split())
    
    if v not in cars or cars[v][0] <= w:
        cars[v] = [w, i+1]
        
for car in cars.values():
    ans += car[1]
    
print(ans)