def has4(number):
    n = number
    while n > 0:
        digit = n%10
        if digit == 4:
            return True
        n = n // 10
    return False

def solve(N, mem):
    result = 0

    for i in range(4, N+1):
        if has4(i):
            result += 1
    return result
#     if N < 3: return 0
#     if N in mem: return mem[N]
#     mem[0] = mem[1] = mem[2] = mem[3] = 0
#     mem[4] = 1
#     for i in range(5, 1000):
#         # if i > 100:
#             # mem[i] = mem[i%100] + (mem[100] * (i // 100))
#         if 4 < i <= 100:
#             n = mem[i-1] + (1 if '4' in str(i) else 0)
#             mem[i] = n
#         elif 100 < i <= 1000:
#             n = mem[i-1]
#     if 100 < i <= 1000:
#         return mem[N % 100] + (19 * (N // 100)) - (19 if N >= 400 else 0) + min(max(0, N-400), 100)
#     return mem[N % 100] + (19 * (N // 100))
# # def fibo(N, fibo_mem):
#     if N in fibo_mem: return fibo_mem[N]
#     if N == 0: return 0
#     if N == 1 or N == 2: return 1

#     result = fibo(N-1, fibo_mem) + fibo(N-2, fibo_mem)
#     fibo_mem[N] = result
#     return fibo_mem[N]
mem = {}
assert solve(399, mem) == 76
assert solve(444, mem) == 121
assert solve(899, mem) == 252
ans = solve(10**6, mem)
assert ans == 468559
# fibo_mem = {}
# fibo(5, fibo_mem)
T = int(input())
# fibo(100, fibo_mem)
for _ in range(T):
    N = int(input())
    ans = solve(N, mem)
    print(ans)