from collections import deque
def solve( A, B):
    adj = {}
    max_val = 0
    for i in range(len(B)):            
        if B[i][0] not in adj:
            adj[B[i][0]] = [B[i][1]]
        else:
            adj[B[i][0]].append(B[i][1])
    
    visited = [0] * (A + 1)
    queue = deque()
    queue.append(1)
    print(adj)
    while queue:
        x = queue.popleft()
        visited[x] = 1 
        for i in adj[x]:
            print(i)
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
        print(visited, queue)
    return visited[A]

A = 3
B =[
  [1, 2],
  [2, 3],
  [3, 1]
]
print(solve(A, B))