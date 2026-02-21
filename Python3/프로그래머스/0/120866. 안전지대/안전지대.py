def solution(board):
    n = len(board)
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for dx in [-1,0,1]:
                    for dy in [-1, 0, 1]:
                        nx = x + dx
                        ny = y + dy
                        
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                            board[nx][ny] = 2
    answer = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                answer +=1
    return answer
