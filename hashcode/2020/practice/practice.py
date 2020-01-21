import heapq
import collections

M, N = [int(x) for x in input().split()]
slices = [int(x) for x in input().split()]

# M, N = [int(x) for x in '100 10'.split()]
# slices = [int(x) for x in '4 14 15 18 29 32 36 82 95 95'.split()]

sortedSlices = sorted(enumerate(slices), key=lambda x: (x[1]))

ans = []
count = 0
idx = 0
pizzas = [[]] * M+1
pizzas[0] = 
for i in range(N):
    idx, s = sortedSlices[i]
    if count + s > M:
        break
    count += s
    ans.append(str(idx))

print(len(ans))
print(' '.join(ans))
