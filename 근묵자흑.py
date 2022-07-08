import sys

N, K = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
start = nums.index(min(nums)) # 최솟값 위치 찾기
ans = sys.maxsize

for idx in range(K):
    front, back = nums[:start-idx], nums[start+K-idx:] # 처음 바꾸는 부분을 기준으로 앞, 뒤를 나눈다
    front_cnt = len(front) // (K-1) + (1 if len(front) % (K-1) else 0) # 앞 부분에서 바뀌는 횟수
    back_cnt = len(back) // (K-1) + (1 if len(back) % (K-1) else 0) # 뒷 부분에서 바뀌는 횟수
    ans = min(ans, front_cnt + back_cnt + 1) # 최솟값 갱신

print(ans)