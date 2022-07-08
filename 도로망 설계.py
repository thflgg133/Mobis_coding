import sys

N, M = map(int, (sys.stdin.readline().split()))

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, t, a, b, c = map(int, sys.stdin.readline().split())

