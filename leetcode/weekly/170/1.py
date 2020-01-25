class Solution:
    def freqAlphabets(self, s: str) -> str:
        ia = ord('a')-1
        buffer = ''
        ans = ''
        for c in s:
            if c == '#':
                if buffer:
                    ans += chr(ia + int(buffer))
                buffer = ''
                continue
                
            ic = int(c)
            if not buffer and ic >= 3 and ic <= 9:
                ans += chr(ia + ic)
                continue
            
            if len(buffer) < 2:
                buffer += c
                continue
            
            ans += chr(ia + int(buffer[0]))
            buffer = buffer[1:] + c
        
        if buffer:
            ans += chr(ia + int(buffer[0]))
            if len(buffer) == 2:
                ans += chr(ia + int(buffer[1]))
            
        return ans

s = Solution()
s.freqAlphabets('1326#')