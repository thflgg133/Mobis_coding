import sys
from collections import deque

def bfs(i,j):
    queue = deque([[i,j]])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx_1[i]
            ny = y + dy_1[i]
            
            if 0 <= nx < W and 0 <= ny < H:
                pass




W, H = map(int, sys.stdin.readline().split())
maps = [list(int, sys.stdin.readline().rstrip()) for _ in range(W)]
visited =[[True] * H for _ in range(W)]

dx_1 = [-1,0,1,0]
dy_1 = [0,-1,0,1]

dx_2 = [-1,-1,-1,0,0,1,1,1]
dy_2 = [-1,0,1,-1,1,-1,0,1]

for i in range(W):
    for j in range(H):
        if maps[i][j] == 'S':
            bfs(i,j)