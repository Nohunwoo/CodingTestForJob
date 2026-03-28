n= int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
count_dict = {}
for card in n_list:
    if card in count_dict:
        count_dict[card] += 1 # 이미 메모된 숫자면 1 추가
    else:
        count_dict[card] = 1  # 처음 보는 숫자면 1로 새로 등록
count_list = []
for i in m_list:
    count_list.append(count_dict.get(i, 0))

print(*count_list)