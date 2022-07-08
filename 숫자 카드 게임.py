import sys

# dp 문제임
N, K= map(int, sys.stdin.readline().split())
    
nums = [i for i in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N)]

for num in nums: # 기준 숫자까지 선택 가능
    for j in range(K+1): #  j 번 뽑기
        for k in range(j): # j 번 뽑은 수들의 합
            pass
    