T = int(input())

for _ in range(T):
    n = int(input())
    fir_open = input().split() # ['A', 'B', 'C', 'D']
    sec_open = input().split() # ['D', 'A', 'B', 'C']
    not_open = input().split() # ['C', 'B', 'A', 'P']
        # fir과 sec 인덱스의 이동에 따라서 not을 바꾼다
    answer = []
    for word in fir_open:
    # 1. 이 단어가 sec_open에서 몇 번째 방(인덱스)으로 쫓겨났는지 찾습니다.
        target_idx = sec_open.index(word)
        # 2. 암호문(not_open)에서 똑같은 방 번호에 있는 단어를 꺼내서 정답 바구니에 담습니다!
        answer.append(not_open[target_idx])
    print(' '.join(answer))