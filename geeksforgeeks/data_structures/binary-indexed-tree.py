

input_array = [2,1,1,3,2,3,4,5,6,7,8,9]
N = len(input_array)
bi_tree = [0] * (N+1)

def update(index, val, N):
    idx = index+1
    # print('idx:',idx)
    while idx < N:
        bi_tree[idx] += val
        idx = idx + (idx & (-idx))
        # print('idx:',idx)

def getSum(bi_tree, index):
    _sum = 0
    idx = index+1
    print('idx:',idx)
    while idx > 0:
        _sum += bi_tree[idx]
        idx = idx - (idx & (-idx))
        print('idx:',idx)
    return _sum

for i, x in enumerate(input_array):
    update(i, x, N)

print(input_array)
print(bi_tree)
print(getSum(bi_tree, 3))
print(getSum(bi_tree, 2))
print(getSum(bi_tree, 8))