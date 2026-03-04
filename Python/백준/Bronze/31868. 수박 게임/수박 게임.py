import sys
input = sys.stdin.readline

level, cherry = map(int, input().split())

watermelon = cherry // (2**(level-1))
print(watermelon)