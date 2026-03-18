tree = []

while True:
    tree = list(map(int, input().split()))
    if tree == [0]:
        break
    leaf = 1
    for i in range(1,len(tree),2):
        leaf *= tree[i]
        real_leaf = leaf - tree[i+1]
        leaf = real_leaf

    print(real_leaf)