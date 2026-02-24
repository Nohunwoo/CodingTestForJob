card, front, back = map(int, input().split())

front_o = front
front_x = card-front
back_o = back
back_x = card-back

front_eq_back = min(front_o,back_o) + min(front_x,back_x)
print(front_eq_back)