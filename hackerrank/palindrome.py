def check_palindrome(text, l, r, mistake = 0):
    is_palindrome = True
    removed_idx = -1

    # print('text: {}, l: {}, r: {}'.format(text,l,r))

    if mistake > 1:
        return False, -1, -1
    
    while r >= l:
        if text[l] == text[r]:
            l += 1
            r -= 1
        else:
            if mistake == 1:
                return False, -1, -1

            is_palindrome_l, _, _ = check_palindrome(text, l+1, r, mistake + 1)
            is_palindrome_r, _, _ = check_palindrome(text, l, r-1, mistake + 1)

            if is_palindrome_l:
                removed_idx = l
                # text = text[:l]+text[l+1:]
                l = l+1
            elif is_palindrome_r:
                removed_idx = r
                # text = text[:r]+text[r+1:]
                r = r-1
            else:
                return False, -1, -1

            mistake += 1
            
    return is_palindrome, mistake, removed_idx

def palindromeIndex(s):

    l, r = 0, len(s)-1
    
    is_palin, mistake, removed_idx = check_palindrome(s, l, r, 0)

    return removed_idx if is_palin and mistake == 1 else -1

print(palindromeIndex('test'))
print(palindromeIndex('aaa'))
print(palindromeIndex('aaab'))
print(palindromeIndex('baa'))
print(palindromeIndex('cbaavaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc'))