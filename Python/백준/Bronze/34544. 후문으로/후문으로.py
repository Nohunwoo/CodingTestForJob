def to_math(floor):
    if floor < 0:
        return floor + 1
    return floor
def to_real(coord):
    if coord <= 0:
        return coord - 1
    return coord

n= int(input())

current_coord = to_math(1)
for i in range(n):
    front, back = map(int, input().split())
    math_front = to_math(front)
    math_back = to_math(back)
    diff = math_back - math_front
    current_coord += diff

print(to_real(current_coord))