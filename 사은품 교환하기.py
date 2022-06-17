import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    ans = 0

    N_cnt = N // 5 # 스페셜 쿠폰을 최소로 쓰는 경우
    M_cnt = (N+M) // 12 # 일반 쿠폰이 없어서 스페셜 쿠폰을 5장 이상 쓰는 경우

    ans = min(N_cnt, M_cnt) # 둘 중 최솟값
    print(ans)