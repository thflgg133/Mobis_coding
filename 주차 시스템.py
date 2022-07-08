import sys
from collections import deque

def bfs(i, j, cnt):
    queue = deque([[i,j]])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M:
                if map[nx][ny] == 0 and visited[nx][ny] == False:
                    cnt += 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])

                elif map[nx][ny] == 2 and visited[nx][ny] == False:
                      cnt -= 2
                      visited[nx][ny] = True
                      queue.append([nx, ny])

            else:
                continue

        ans.append(cnt)


N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(M):
        if map[i][j] != 1 and visited[i][j] == False:
            cnt = 0
            bfs(i, j, cnt)

if ans:
  print(max(ans))

else:
  print(0)