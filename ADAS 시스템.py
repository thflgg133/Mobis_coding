import sys

def bfs():
    pass



W, H = map(int, sys.stdin.readline().split())
maps = [list(int, sys.stdin.readline().rstrip()) for _ in range(W)]
visited =[[True] * H for _ in range(W)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(W):
    for j in range(H):
        if maps[i][j] == 'S':
            bfs()