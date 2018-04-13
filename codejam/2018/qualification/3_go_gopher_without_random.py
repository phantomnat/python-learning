import sys
import math

max_width = 0
max_height = 0
orchard_map = ''
area = 0

def cal_max_width_height(area):
    max_w = int(math.ceil(math.sqrt(area)))
    max_h = max_w
    while True:
        if (max_h - 1) * max_w >= area:
            max_h -= 1
        else: 
            break
    return max_w, max_h

def _2d_to_1d(x, y):
    global max_width
    return ((y - 1) * max_width) + (x - 1)

def _1d_to_2d(n):
    global max_width
    x = (n % max_width) + 1
    y = int(n / max_width) + 1
    return x, y

def dig(x, y):
    global orchard_map
    global max_width

    n = _2d_to_1d(x, y)

    if orchard_map[n] == '-':
        orchard_map = orchard_map[0:n] + 'X' + orchard_map[n+1:]

def point_to_3x3p(x, y):
    return int(math.ceil(x / 3)), int(math.ceil(y / 3))

def _3x3p_to_center(x3, y3):
    return ((3 * x3) - 1), ((3 * y3) - 1)

def check_3x3_dug(x, y):
    # row1 := c_x - 1, c_y - 1 => c_x + 1, c_y - 1
    # row2 := c_x - 1, c_y     => c_x + 1, c_y
    # row3 := c_x - 1, c_y + 1 => c_x + 1, c_y + 1
    for i in [-1, 0, 1]:
        start_x = x - 1
        end_x = x + 1
        start_1d = _2d_to_1d(start_x, y + i)
        end_1d = _2d_to_1d(end_x, y + i)
        _1x3_orchard = orchard_map[start_1d:end_1d + 1]
        if _1x3_orchard.find('-') >= 0:
            return False
    return True

def get_next_dig():
    global max_width
    global max_height
    global area
    global orchard_map

    n = 0
    x = 0
    y = 0
    idx = 0
    while True:
        n = orchard_map.find('-', idx)
        if n == -1: 
            break

        x, y = _1d_to_2d(n)
        
        # get 3x3 coordinate
        x3, y3 = point_to_3x3p(x, y)
        c_x, c_y = _3x3p_to_center(x3, y3)

        if x3 * 3 > max_width:
            c_x = max_width - 1
            x3 = -1
        if y3 * 3 > max_height:
            c_y = max_height - 1
            y3 = -1
            
        return c_x, c_y

# def view_orchard(i):
#     global orchard_map
#     global max_width
#     with open('3_case_{}.txt'.format(i), 'w') as fout:
#         for i in range(0, len(orchard_map), max_width):
#             fout.write(orchard_map[i:i+max_width] + '\n')

t = int(input())

for i in range(1, t + 1):

    a = int(input())
    area = a

    max_width, max_height = cal_max_width_height(a)
    orchard_map = '-' * max_width * max_height

    dig_cmd = get_next_dig()
    
    cb = 0
    while True:
        # send coordinate 
        x, y = dig_cmd
        print('{} {}'.format(x, y))

        # read go gopher output
        x, y = [int(s) for s in input().split(" ")]

        if (x == 0 and y == 0) or (x == -1 and y == -1):
            break

        dig(x, y)
        
        # view_orchard(i)

        if check_3x3_dug(x, y):
            dig_cmd = get_next_dig()
            
