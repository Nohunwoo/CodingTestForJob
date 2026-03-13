# Bronze 3

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

max_num = -1
max_row = 0  
max_col = 0

for i in range(9):
    for j in range(9):
        if board[i][j] > max_num:
            max_num = board[i][j]
            max_row = i
            max_col = j
        else:
            continue

print(max_num)
print(f'{max_row+1} {max_col+1}')