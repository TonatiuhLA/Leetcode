class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = {}
        ret = 0

        for ch in s:
            chars[ch] = chars[ch] + 1 if ch in chars else 1
        
        truke = False
        for key, val in chars.items():
            if val % 2 != 0:
                if truke:
                    ret += val - 1
                else:
                    ret += val
                    truke = True
            else:
                ret += val
        return ret