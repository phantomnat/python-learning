

# def check_valid(cake):
    
class Solution:
    
    def canCutWaffle(self, r, c, h, v, waffle):
        ans = 'POSSIBLE'
        # cutted_waffle = []
        chips = 0
        pieces = (h + 1) * (v + 1)
        for w in waffle:
            chips += w.count('@')
            # for c in w:
            #     if c == '@':
            #         chips += 1
        # print('chips:',chips,' pieces:',pieces)
        # simple calc
        if chips == 0:
            pass
        elif chips < pieces or chips % pieces != 0:
            # impossible
            ans = 'IMPOSSIBLE'
        else:
            # try every possible
            if not self.cut(waffle, chips // pieces, r, c, h, v, [], [], 0, 0):
                ans = 'IMPOSSIBLE'
                    
        return ans
    def cut(self, waffle, chips_per_piece, r, c, h, v, h_cut = [], v_cut = [], h_start = 0, v_start = 0):
        if len(h_cut) == h and len(v_cut) == v:
            # print(h_cut, v_cut)
            pieces = [0 for x in range((h + 1) * (v + 1))]
            # start_h
            # next_h
            # cutting waffle
            # cutted_waffle = [[]]
            for j, w in enumerate(waffle):
                for i, p in enumerate(w):
                    if p != '@':
                        continue

                    # convert to pieces coordinate
                    p_x = p_y = p_coor = 0
                    for xi, x in enumerate(v_cut):
                        if i <= x:
                            p_x = xi
                            break
                        elif xi == len(v_cut) - 1:
                            p_x = xi + 1
                    for yi, y in enumerate(h_cut):
                        if j <= y:
                            p_y = yi
                            break
                        elif yi == len(h_cut) - 1:
                            p_y = yi + 1
                        # if 
                    p_coor = (p_y * (v+1)) + p_x
                    pieces[p_coor] += 1
                    # print('j: {}, i: {},  --  p_x: {}, p_y: {}, pcor: {}'.format(j,i,p_x, p_y, p_coor), v_cut, h_cut)
            # validate
            # c = 0
            # print(min(pieces), max(pieces), chips_per_piece)
            # if min(pieces) == max(pieces) == chips_per_piece:
                # print('success!')
            return min(pieces) == max(pieces) == chips_per_piece

        for i in range(h_start, r-1):
            if len(h_cut)+1 <= h:
                h_cut.append(i)
            for j in range(v_start, c-1):
                # print('j=',j, ' ', v_cut)
                if len(v_cut)+1 <= v:
                    v_cut.append(j)
                if (self.cut(waffle,chips_per_piece, r, c, h, v, h_cut, v_cut, i+1, j+1)):
                    return True
                if len(v_cut) > 0:
                    v_cut.pop()
            if len(h_cut) > 0:
                h_cut.pop()
        return False
        # if r_cut < h:
            # self.cut(r, c, h, v, r_cut + 1, c_cut)

s = Solution()
stdin = True

if stdin:
    t = int(input())
    for i in range(1, t+1):
        
        r, c, h, v = [int(s) for s in input().split()]
        ans = 'POSSIBLE'
        chips = 0
        pieces = (h + 1) * (v + 1)
        waffle = []
        
        for _ in range(r):
            w = input()
            chips += w.count('@')
            waffle.append(w)

        # print('chips:',chips,' pieces:',pieces)
        # simple calc
        if chips == 0:
            pass
        elif chips < pieces or chips % pieces != 0:
            # impossible
            ans = 'IMPOSSIBLE'
        else:
            # try every possible
            if not s.cut(waffle, chips // pieces, r, c, h, v, [], [], 0, 0):
                ans = 'IMPOSSIBLE'
                    
        # ans = 'IMPOSSIBLE'

        # cutted_waffle = []
        # chips = 0
        # pieces = (h + 1) * (v + 1)

        # for _ in range(r):
        #     w = input()
        #     waffle.append(w)

        # ans = s.canCutWaffle(r, c, h, v, waffle)
        # simple calc
        # if chips == 0:
        #     ans = 'POSSIBLE'
        # elif chips < pieces or chips % pieces != 0:
        #     # impossible
        #     pass
        # else:
        #     # try every possible
        #     pass

        print('Case #{}: {}'.format(i, ans))
else:

    # print(s.canCutWaffle(3,6,1,1, ['.@@..@','.....@','@.@.@@']))
    print(s.canCutWaffle(3,4,2,2, ['@.@@','@@.@','@.@@']))
