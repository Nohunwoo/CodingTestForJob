from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    q = deque([(0,0)])
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m :
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    q.append((nr, nc))
    
    answer = maps[n-1][m-1]
    return answer if answer > 1 else -1