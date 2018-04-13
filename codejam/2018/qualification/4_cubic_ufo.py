import math

PI_1_DEG = math.pi / 180
SQRT_OF_2 = math.sqrt(2)

t = int(input())

def print_coordinate(i, deg1, deg2 = 0):
    global PI_1_DEG
    p1x = 0.5 * math.cos(deg1 * PI_1_DEG)
    p1y = 0.5 * math.sin(deg1 * PI_1_DEG) * math.cos(deg2 * PI_1_DEG)
    p1z = -0.5 * math.sin(deg2 * PI_1_DEG)
    p2x = -0.5 * math.sin(deg1 * PI_1_DEG)
    p2y = 0.5 * math.cos(deg1 * PI_1_DEG) * math.cos(deg2 * PI_1_DEG)
    p2z = -0.5 * math.sin(deg2 * PI_1_DEG)
    p3x = 0
    p3y = 0.5 * math.sin(deg2 * PI_1_DEG)
    p3z = 0.5 * math.cos(deg2 * PI_1_DEG)

    print("Case #{}:".format(i))
    print('{} {} {}'.format(p1x if p1x != 0 else 0, p1y if p1y != 0 else 0, p1z if p1z != 0 else 0))
    print('{} {} {}'.format(p2x if p2x != 0 else 0, p2y if p2y != 0 else 0, p2z if p2z != 0 else 0))
    print('{} {} {}'.format(p3x if p3x != 0 else 0, p3y if p3y != 0 else 0, p3z if p3z != 0 else 0))

def cal_area_xy(deg):
    global PI_1_DEG
    return math.sin(PI_1_DEG * deg) + math.cos(PI_1_DEG * deg)
    
def find_area(a, min_a, max_a, low_deg, high_deg):
    while True:
        half_deg = (high_deg - low_deg) * 0.5
        # print(half_deg)
        low_area = cal_area_xy(low_deg)
        half_area = cal_area_xy(low_deg + half_deg)
        high_area = cal_area_xy(high_deg)
    
        if half_area > min_a and half_area < max_a:
            return low_deg + half_deg
        elif a > low_area and a < half_area:
            high_deg = low_deg + half_deg
        elif a > half_area and a < high_area:
            low_deg = low_deg + half_deg
        else:
            print('error')
            break

def cal_area_xyz(deg2):
    # with deg1 = 45
    global PI_1_DEG
    global SQRT_OF_2
    return (math.cos(PI_1_DEG * deg2) * SQRT_OF_2) + (SQRT_OF_2 * math.sin(PI_1_DEG * 45) * math.sin(PI_1_DEG * deg2))
    
def find_area_with_deg2(a, min_a, max_a, low_deg2, high_deg2):
    while True:
        half_deg2 = (high_deg2 - low_deg2) * 0.5
        # print(half_deg)
        low_area = cal_area_xyz(low_deg2)
        half_area = cal_area_xyz(low_deg2 + half_deg2)
        high_area = cal_area_xyz(high_deg2)
    
        if half_area > min_a and half_area < max_a:
            return low_deg2 + half_deg2
        elif a > low_area and a < half_area:
            high_deg2 = low_deg2 + half_deg2
        elif a > half_area and a < high_area:
            low_deg2 = low_deg2 + half_deg2
        else:
            print('error')
            break
    
for i in range(1, t + 1):
    a = float(input())
    min_a = a - 0.0000005
    max_a = a + 0.0000005

    deg = 0.0
    deg2 = 0.0
    found_ans = False

    if a > 1.414213562373095:
        # implement later
        deg = 45
        
        low_a = 0
        low_deg2 = -1
        high_a = 2
        high_deg2 = -1

        max_deg2 = 35.26439
        for j in range(1, 3526):
            deg2 = (j / 10.0)
            area = (math.cos(PI_1_DEG * deg2) * SQRT_OF_2) + \
                (SQRT_OF_2 * math.sin(PI_1_DEG * 45) * math.sin(PI_1_DEG * deg2))
            if min_a < area and area < max_a:
                # deg2 = 
                found_ans = True
                break
            if area > low_a and area < a:
                low_a = area
                low_deg2 = deg2
            if area < high_a and area > a:
                high_a = area
                high_deg2 = deg2

        if not found_ans:
            deg2 = find_area_with_deg2(a, min_a, max_a, float(low_deg2), float(high_deg2))
    else:
        low_a = 0
        low_idx = -1
        high_a = 2
        high_idx = -1

        for j in range(46):
            area = math.sin(PI_1_DEG * j) + math.cos(PI_1_DEG * j)
            if min_a < area and area < max_a:
                deg = j
                found_ans = True
                break
            if area > low_a and area < a:
                low_a = area
                low_idx = j
            if area < high_a and area > a:
                high_a = area
                high_idx = j

        if not found_ans:
            deg = find_area(a, min_a, max_a, float(low_idx), float(high_idx))

    print_coordinate(i, deg, deg2)
    
