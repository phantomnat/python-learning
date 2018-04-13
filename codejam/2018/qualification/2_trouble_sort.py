t = int(input())
# ok_cnt = 0
for j in range(1, t + 1):
    n = int(input())
    num_list = [int(s) for s in input().split(" ")]
    ans = 'OK'

    odd_list = num_list[::2]
    even_list = num_list[1::2]

    even_len = len(even_list)
    odd_len = len(odd_list)

    even_list.sort()
    odd_list.sort()

    for i in range(odd_len):
        odd_num = odd_list[i]
        even_num = even_list[i] if i < even_len else None
        next_odd_num = odd_list[i + 1] if i + 1 < odd_len else None
        if even_num is None:
            break
        
        if odd_num > even_num:
            ans = (2 * i)
            break
        elif next_odd_num is not None and even_num > next_odd_num:
            ans = (2 * i) + 1
            break

    # if ans == 'OK': ok_cnt += 1
    # if ans == 0 or ans == 'OK':
    #     print(odd_list[0:5])
    #     print(even_list[0:5])

    print('Case #{}: {}'.format(j, ans))
    # print('Case #{}: {} , len={}'.format(j, ans, len(num_list)))
# print('OK set: {}'.format(ok_cnt))