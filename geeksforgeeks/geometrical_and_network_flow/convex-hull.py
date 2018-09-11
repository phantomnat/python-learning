# https://practice.geeksforgeeks.org/problems/convex-hull/0

class ConvexPt(object):
    def __init__(self, pt, next_pt = None, prev_pt = None):
        self.pt = pt
        self.next_pt = next_pt
        self.prev_pt = prev_pt
    def set_next(self, pt):
        self.next_pt = pt
    def set_prev(self, pt):
        self.prev_pt = pt

_c = ConvexPt((1,1))
assert _c.pt == (1,1)
# print(id(_c))
# print(id((1,1)))
def orientation(p, r, q):
    return ((r[1]-p[1])*(q[0]-r[0]))-((q[1]-r[1])*(r[0]-p[0]))
def is_ccw(p, r, q):
    return orientation(p, r, q) < 0

def solve(coor_list, left_pt):
    
    l = ConvexPt(left_pt)
    cvh_list = []
    cvh_list.append(l.pt)
    p = l
    # get_list = lambda x, p: for pt in x:
    # search_coor_list = coor_list[:]
    while True:
        q = next((x for x in coor_list if x != p.pt), None)
        if q is None: 
            return []
        for pt in coor_list:
            if pt == q or pt == p.pt:
                continue
            if is_ccw(p.pt, pt, q):
                q = pt

        if l.pt == q:
            break
        cvh = ConvexPt(q, None, p)
        p.set_next(cvh)
        p = cvh
        cvh_list.append(cvh.pt)
        
    return cvh_list

T = int(input())

for _ in range(T):
    N = int(input())
    xy_array = [int(s) for s in input().split()]
    while len(xy_array) < N*2:
        xy_array += [int(s) for s in input().split()]
    coor_list = []
    left_pt = (1000, 0)
    # array =
    for i, p in enumerate(xy_array):
        if i%2 == 0:
            _x = int(p)
        else:
            pt = (_x, int(p))
            if pt[0] < left_pt[0]:
                left_pt = pt
            coor_list.append(pt)
    ans = -1

    if N > 2:
        cvh = solve(coor_list, left_pt)
        if len(cvh) > 2:
            cvh.sort(key=lambda x: (x[0], x[1]))
            ans = ', '.join(['{} {}'.format(x[0], x[1]) for x in cvh])

    print(ans)
        
'''
For Input:
2
7
789 179 404 585 755 652 933 400 677 61 740 369 227 13 
7
540 95 571 796 379 435 602 468 903 98 493 318 757 653
Your Output is:
227 13, 404 585, 677 61, 755 652, 789 179, 933 400
379 435, 540 95, 571 796, 757 653, 903 98
Output of Online Judge is:
227 13, 404 585, 677 61, 755 652, 789 179, 933 400
379 435, 540 95, 571 796, 757 653, 903 98

Input:
30
582 544 769 124 640 188 439 644 395 989 681 321 487 99 753 19 99 464 11 696 180 506 67 143 426 99 979 473 967 854 749 798 273 548 87 517 160 913 901 878 198 554 4 933 952 36 499 108 155 50 907 862 4 335 785 326 798 429 634 764

Its Correct output is:
4 335, 4 933, 67 143, 155 50, 395 989, 753 19, 901 878, 952 36, 967 854, 979 473

And Your Code's output is:
4 933, 4 335, 67 143, 155 50, 395 989, 753 19, 901 878, 952 36, 967 854, 979 473
'''