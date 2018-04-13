t = int(input())

def dmg_calc(text):
    dmg = 0
    c_dmg = 1
    for c in text:
        if c == 'C':
            c_dmg *= 2
        elif c == 'S':
            dmg += c_dmg
    return dmg

for i in range(1, t + 1):
    d, p = input().split(" ")
    ans = 'IMPOSSIBLE'
    shield = int(d)
    total_dmg = 0
    s_cnt = 0
    c_cnt = 0
    current_dmg = 1
    # atk_seq = {}

    for j, c in enumerate(p):
        if c == 'C':
            current_dmg *= 2
            c_cnt += 1
            # atk_seq[j] = {'t': 'C', 'd': current_dmg}
        elif c == 'S':
            s_cnt += 1
            total_dmg += current_dmg
            # atk_seq[j] = {'t': 'S', 'd': current_dmg}
    
    if total_dmg <= shield:
        ans = 0
    elif c_cnt > shield:
        # impossible
        pass
    else:
        hack_cnt = 0
        k = 0
        while True:
            r_pos = p.rfind('CS')
            if r_pos == -1:
                break
            p = p[0:0+r_pos] + 'SC' + p[r_pos+2:]
            hack_cnt += 1
            total_dmg = dmg_calc(p)
            if total_dmg <= shield:
                ans = hack_cnt
                break
            k += 1

    print('Case #{}: {}'.format(i, ans))
