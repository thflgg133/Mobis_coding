import sys
from collections import deque

def bfs(i,j):
    queue = deque([[i,j, None]])
    score = 0

    while queue:
        if queue[0][2] == 'P':
            x, y, z = queue.popleft()
        
        else:
            x, y, z = queue.pop()

        visited[x][y] = True

        # 시작점에서는 점수 계산 안함
        if maps[x][y] == 'S':
            pass

        else:
            # 위험 점수 계산
            if maps[x][y] == 'P':
                for i in range(8):
                    nx_2 = x + dx_2[i]
                    ny_2 = y + dy_2[i]
            
                    if 0 <= nx_2 < W and 0 <= ny_2 < H:
                        if maps[nx_2][ny_2] == 'P':
                            score += 1 

                score -= 3

            else:
                for i in range(8):
                    nx_2 = x + dx_2[i]
                    ny_2 = y + dy_2[i]

                    if 0 <= nx_2 < W and 0 <= ny_2 < H:
                        if maps[nx_2][ny_2] == 'P':
                            score += 1 
            
        # 이동
        for i in range(4):
            nx_1 = x + dx_1[i]
            ny_1 = y + dy_1[i]
            
            if 0 <= nx_1 < W and 0 <= ny_1 < H:
                if maps[nx_1][ny_1] == 'E':
                    if score < 0:
                        return 0

                    else:
                        return score
                
                else:
                    # 'P'가 우선순위이기 때문에 'P'는 queue의 왼쪽으로 일반점은 오른쪽으로 넣어준다
                    if visited[nx_1][ny_1] == False and maps[nx_1][ny_1] == 'P':
                        queue.appendleft([nx_1, ny_1, 'P'])
                        

                    elif visited[nx_1][ny_1] == False and maps[nx_1][ny_1] != 'P':
                        queue.append([nx_1, ny_1, None])


W, H = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(W)]
visited =[[False] * H for _ in range(W)]

# 원래는 상 -> 좌 -> 우 -> 하 인데 queue에 담기는 우선순위를 고려해 반대로 저장
dx_1 = [1,0,0,-1]
dy_1 = [0,1,-1,0]

# 위험 점수 탐색을 위한 방향 설정
dx_2 = [-1,-1,-1,0,0,1,1,1]
dy_2 = [-1,0,1,-1,1,-1,0,1]

for i in range(W):
    for j in range(H):
        if maps[i][j] == 'S':
            ans = bfs(i,j)
            break

print(ans)