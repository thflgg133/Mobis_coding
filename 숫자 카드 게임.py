import sys
from itertools import combinations

N, K= map(int, sys.stdin.readline().split())
    
arr = [i for i in range(N)]
dp = [[0 for _ in range(N)] for _ in range(K+1)]
print(dp)

for i in range(N):
    for j in range(K+1):
        