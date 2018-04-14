import math
T = int(input())

def optimum_atk(Hk, Ad, B):
    turn = math.ceil(Hk / Ad)
    i = 1
    while B > 0:
        t = math.ceil(Hk / (Ad + (B * i))) + i
        if t >= turn:
            return t
        turn = t
        i += 1
    return turn

def calc_heal_every_turn(Hd, Ak):
    return math.inf if Ak <= 0 else math.ceil(Hd / Ak) - 1
    
for i in range(1, T+1):
    Hd, Ad, Hk, Ak, B, D = [int(s) for s in input().split()]

    HP = Hd
    last_action = ''
    turn_count = 0
    is_win = False

    optimal_turn_for_atk = optimum_atk(Hk, Ad, B)

    # calc for debuff
    # debuff_tables = {}
    he_list = []

    # HE = math.ceil(Hd / Hk) - 1
    # debuff_tables[need_to_heal_every_turn] = 0
    # # nthet = need_to_heal_every_turn
    # prev_HE = need_to_heal_every_turn
    # prev_HE_turn = 0
    # he = need_to_heal_every_turn + 1
    # last_he_turn = 0

    HEi = 0
    prev_HE = None
    HET = math.ceil(Hd / Ak) - 1
    p_he = HET
    last_min_turn = min_turn = 0
    while D > 0:
        # find minimum debuff
        if D * HEi >= Ak:
            he_list.append({'he':math.inf,'t_diff':HEi-last_min_turn})
            break
        he = math.ceil(Hd / (Ak - (D * HEi))) - 1
        if p_he != he:
            # found minimum buff
            min_turn = HEi
            he_list.append({'he':he,'turn':min_turn,'t_diff':min_turn-last_min_turn})
            # debuff_tables[he] = min_turn
            last_min_turn = min_turn
            p_he = he
        HEi += 1

    # print(debuff_tables)
    # exit()

    # print('Optimal Atk: ', 'B={} A={}'.format(i, math.ceil(Hk / (Ad + (B * i)))))
    predict_win = False
    turn_count = 0


    next_he = None
    prev_he = calc_heal_every_turn(Hd, Ak)

    while True:
        turn_count += 1
        # action = ''
        # dragon_turn_to_win = math.inf if Ad <= 0 else math.ceil(Hk / Ad)
        # knight_turn_to_end = math.inf if Ak <= 0 else math.ceil(HP / Ak)
        # predict_turn_end = min(dragon_turn_to_win, knight_turn_to_end)

        cur_he = calc_heal_every_turn(Hd, Ak)
        cur_optimum_atk = optimum_atk(Hk, Ad, B)

        # if cur_he == 1 and D <= 0: 
        #     # not possible to win
        #     break
        
        atk_heal_turn_to_win = math.inf if cur_he <= 1 else \
            cur_optimum_atk + math.ceil((cur_optimum_atk - 2) / (cur_he - 1)) - 1

        if len(he_list) > 0 and (next_he is None or next_he['he'] == cur_he):
            # cur_he = next_he
            next_he = he_list.pop(0)

        next_debuff_to_win = math.inf
        if next_he is not None and next_he['he'] != cur_he:
            # calc if we try to decrease enemy atk
            next_debuff_to_win = next_he['t_diff'] + cur_optimum_atk
            if next_he['he'] != math.inf:
                next_debuff_to_win += 1
            if cur_he >= 2:
                next_debuff_to_win += math.ceil((next_he['t_diff'] - 2) / (cur_he - 1)) - 1
                next_debuff_to_win += math.ceil((cur_optimum_atk - 1) / (cur_he)) - 1
        
        action = 'A'
        if next_debuff_to_win < atk_heal_turn_to_win:
            # try debuff
            action = 'D'
        else:
            # attack!!!
            dragon_turn_to_win = math.inf if Ad <= 0 else math.ceil(Hk / Ad)
            buff_dragon_turn_to_win = math.inf if B <= 0 else math.ceil(Hk / (Ad + B)) + 1
            if dragon_turn_to_win > buff_dragon_turn_to_win:
                action = 'B'

        # override action for heal
        if (action == 'D' and (Ak-D) >= HP) or (action != 'D' and Ak >= HP and Ad < Hk):
            action = 'C'

        # print('atk_heal_turn_to_win')
        # heal_knight_turn_to_end = math.inf if Ak <= 0 else math.ceil(Hd / Ak)
        # buff_dragon_turn_to_win = math.inf
        # debuff_knight_turn_to_end = 0
        # is_win_by_debuff = is_win_by_buff = False
        # if D > 0 and Ak > 0:
        #     debuff_knight_turn_to_end =  math.inf if Ak <= 0 else math.ceil(HP / (Ak-D))
        #     is_win_by_debuff = (debuff_knight_turn_to_end >= dragon_turn_to_win) \
        #         or (debuff_knight_turn_to_end >= optimal_turn_for_atk)
        # if B > 0:
        #     buff_dragon_turn_to_win = math.ceil(Hk / (Ad + B)) + 1
        #     is_win_by_buff = (buff_dragon_turn_to_win <= knight_turn_to_end) or \
        #         (buff_dragon_turn_to_win <= optimal_turn_for_atk)

        # action = 'A'

        
        # if D > 0 and Ak > 0:
        #     debuff_knight_turn_to_end = math.inf if Ak-D <= 0 else (math.ceil(HP / (Ak-D)) + 1)
        #     is_win_by_debuff = dragon_turn_to_win <= debuff_knight_turn_to_end
        #     debuff_predict_turn_end = min(dragon_turn_to_win, debuff_knight_turn_to_end)
        
        # if not predict_win:
        #     # if is_win_by_debuff or debuff_knight_turn_to_end is not math.inf \
        #     #     and knight_turn_to_end < debuff_knight_turn_to_end:
        #     #     action = 'D'
        #     # elif is_win_by_buff or buff_dragon_turn_to_win is not math.inf \
        #     #     and dragon_turn_to_win > buff_dragon_turn_to_win:
        #     #     action = 'B'
            
        #     if is_win_by_debuff \
        #         or debuff_knight_turn_to_end >= optimal_turn_for_atk:
        #         action = 'D'
        #         predict_win = True
        #     elif is_win_by_buff: 
        #         action = 'B'
        #         predict_win = True
        #     elif heal_knight_turn_to_end >= optimal_turn_for_atk:
        #         action = 'C'
        #         predict_win = True
        #     elif debuff_knight_turn_to_end >= knight_turn_to_end:
        #         action = 'D'
        # else:
        #     # predicts = [heal_predict_end, buff_predict_turn_end, debuff_predict_turn_end]
        #     # predicts_min_val = min(predicts)
        #     # predicts_min_idx = predicts.index(predicts_min_val)
        #     # buff_dragon_turn_to_win = math.ceil(Hk / (Ad + B)) + 1
        #     #     is_win_by_buff = buff_dragon_turn_to_win <= knight_turn_to_end
        #     #     buff_predict_turn_end = min(buff_dragon_turn_to_win, knight_turn_to_end)
            
        #     if dragon_turn_to_win > buff_dragon_turn_to_win:
        #         action = 'B'
            # if predicts_min_val < predict_turn_end:
            #     if predicts_min_idx == 0: action = 'C'
            #     elif predicts_min_idx == 1: action = 'B'
            #     else: aciton = 'D'
            
        #     if buff_predict_turn_end < predict_turn_end:
        #         action = 'B'
        #         predict_turn_end = buff_predict_turn_end
        #     if debuff_predict_turn_end < predict_turn_end:
        #         action = 'D'
        #         predict_turn_end = 
        # elif buff_predict_turn_end < predict_turn_end:
        #     action = 'B'
        # elif debuff_predict_turn_end < predict_turn_end:
        #     action = 'D'
        
        # print('action:',action)
        if action == 'C':
            if last_action == action:
                break
            HP = Hd
        elif action == 'A':
            Hk -= Ad
            if Hk <= 0: 
                is_win = True
                break
        elif action == 'B':
            Ad += B
        elif action == 'D':
            Ak = 0 if D > Ak else Ak - D

        if HP <= Ak: 
            break
        else: HP -= Ak

        last_action = action
        
    ans = 'IMPOSSIBLE' if not is_win else turn_count

    print('Case #{}: {}'.format(i, ans))