# https://practice.geeksforgeeks.org/problems/check-if-two-line-segments-intersect/0

T = int(input())

def find_orientation(pts):
    p1, p2, p3 = pts
    o = ((p2[1]-p1[1]) * (p3[0]-p2[0])) - ((p3[1]-p2[1]) * (p2[0]-p1[0]))
    if o == 0: return 0
    return 1 if o > 1 else -1
def on_segment(start_pt, mid_pt, end_pt):
    if min(start_pt[0],end_pt[0]) <= mid_pt[0] <= max(start_pt[0], end_pt[0]) and \
        min(start_pt[1],end_pt[1]) <= mid_pt[1] <= max(start_pt[1], end_pt[1]):
        return True
    return False
def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    o1 = find_orientation([(x1, y1), (x2, y2), (x3, y3)])
    o2 = find_orientation([(x1, y1), (x2, y2), (x4, y4)])
    o3 = find_orientation([(x3, y3), (x4, y4), (x1, y1)])
    o4 = find_orientation([(x3, y3), (x4, y4), (x2, y2)])

    if o1 != o2 and o3 != o4:
        return 1
    # special case
    # colinear
    if o1 == 0 and on_segment((x1, y1), (x3, y3), (x2, y2)):
        return 1
    if o2 == 0 and on_segment((x1, y1), (x4, y4), (x2, y2)):
        return 1
    if o3 == 0 and on_segment((x3, y3), (x1, y1), (x4, y4)):
        return 1
    if o4 == 0 and on_segment((x3, y3), (x2, y2), (x4, y4)):
        return 1
    return 0

# is_intersect(10, 0, 0, 10, 0, 0, 10, 10)

for _ in range(T):
    x1, y1, x2, y2 = [int(s) for s in input().split()]
    x3, y3, x4, y4 = [int(s) for s in input().split()]

    ans = is_intersect(x1, y1, x2, y2, x3, y3, x4, y4)

    print(ans)
    