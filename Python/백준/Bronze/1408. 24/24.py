import sys
input = sys.stdin.readline

real_time = input().strip()
start_time = input().strip()

r_h, r_m, r_s = map(int, real_time.split(':'))
s_h, s_m, s_s = map(int, start_time.split(':'))

real_sec = r_h * 3600 + r_m * 60 + r_s
start_sec = s_h * 3600 + s_m * 60 + s_s

left_sec = start_sec - real_sec

if left_sec < 0:
    left_sec += 24 * 3600 

ans_h = left_sec // 3600
ans_m = (left_sec % 3600) // 60
ans_s = left_sec % 60

print(f'{ans_h:02d}:{ans_m:02d}:{ans_s:02d}')