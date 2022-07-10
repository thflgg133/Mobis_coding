import sys
import heapq
INF = sys.maxsize

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        cost, now = heapq.heappop(heap)
        
        if distance[now] < cost:
            continue
        
        for next_node, *weight in graph[now]:
            next_cost = cost + min(*weight)
            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))
            


N, M = map(int, (sys.stdin.readline().split()))

graph = [[] for _ in range(N+1)]

for i in range(M):
    s, t, a, b, c = map(int, sys.stdin.readline().split())
    
    if s == 1:
        graph[s].append((t,a,b))

    elif t == N:
        graph[s].append((t,b,c))
        
    else:
        graph[s].append((t,a,b,c))

print(graph)

for i in range(1, N+1):   
    distance = [INF] * (N+1)
    dijkstra(i)
    print(distance)