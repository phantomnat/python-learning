import math
T = int(input())

for i in range(1, T+1):
    N, P = [int(s) for s in input().split(' ')]
    R = [int(s) for s in input().split(' ')]
    Q = {}
    for j in range(N):
        Q[j] = []
        for s in input().split(' '):
            Qi = int(s) / float(R[j])
            Qs = set()
            # Qmax = Qi * 1.1
            # Qmin = Qi * 0.9
            lower = int(Qi)
            upper = int(math.ceil(Qi))
            if (upper+1) * 1.1 >= Qi and (upper+1) * 0.9 <= Qi: Qs.add(upper+1)
            if upper * 1.1 >= Qi and upper * 0.9 <= Qi: Qs.add(upper)
            if lower * 1.1 >= Qi and lower * 0.9 <= Qi: Qs.add(lower)
            if (lower-1) * 1.1 >= Qi and (lower-1) * 0.9 <= Qi: Qs.add(lower-1)
            Q[j].append(Qs)
    
    print(R)
    print(Q)

    

