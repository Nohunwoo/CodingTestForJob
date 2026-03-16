word_list = []
for _ in range(5):
    word = list(input())
    word_list.append(word)

new_list = []
for i in range(15):
    for j in range(5):
        if i < len(word_list[j]):
            new_list.append(word_list[j][i])

print(''.join(new_list))