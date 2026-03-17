import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = "1" * (k - 1) + str(n)

print(answer)