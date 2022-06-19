import sys
from itertools import combinations

'''
N, K = map(int, sys.stdin.readline().split())

arr = list(combinations([i % N for i in range(N)], K))
ans = 0

for i in range(len(arr)):
    if sum(arr[i]) % N == 0:
        ans += 1

print(ans)
'''

N, K = map(int, sys.stdin.readline().split())

arr = [i for i in range(N)]
print(arr)

# Idea
# 1. N값을 기준으로 배열안에 있는 수로 나올수 있는 나머지를 구한다??