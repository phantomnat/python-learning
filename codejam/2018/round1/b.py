t = int(input())

# def process(cashiers, carried_robots, ci):
#     n_cashiers = len(cashiers)
#     n_robots = len(carried_robots)

#     max_robots_per_cashier = n_robots

#     for i in range(max_robots_per_cashier):
        

def gen(robots = [], robot_no, total_robots, bits):
    if robot_no == total_robots - 1:
        robots[robot_no] = bits
        # process

        return 


for i in range(1, t+1):

    robots, bits, cashiers = [int(s) for s in input().split()]
    cashiers_data = []
    for _ in range(len(cashiers)):
        max_bits, bps, pt = [int(s) for s in input().split()]
        cashiers_data.append({'m':max_bits, 'bps':bps, 'pt':pt})

    for robot in len(robots):
        b = bits

    gen([], robot_no, bits)
    ans = 0

    print('Case #{}: {}'.format(i, ans))