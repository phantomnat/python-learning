# Complete the anagram function below.
def anagram(s):
    n = len(s)
    if n % 2 == 1:
        return -1

    l = s[:(n//2)]
    r = s[(n//2):]
    # print(l, r)
    l_dict = {}
    r_dict = {}
    for c in l:
        if c in l_dict: l_dict[c] += 1
        else: l_dict[c] = 1
    for c in r:
        if c in r_dict: r_dict[c] += 1
        else: r_dict[c] = 1
    
    diff = 0
    for i in range(ord('a'), ord('z')+1):
        # print(chr(i))
        char = chr(i)
        l_cnt = 0 if char not in l_dict else l_dict[char] 
        r_cnt = 0 if char not in r_dict else r_dict[char] 
        diff += int(abs(l_cnt - r_cnt))
    # print(l_dict)
    # print(r_dict)
    # print(diff)
    return diff // 2

print(anagram('aaabbb'))
print(anagram('ab'))
print(anagram('abc'))
print(anagram('mnop'))
print(anagram('xyyx'))
print(anagram('xaxbbbxx'))


