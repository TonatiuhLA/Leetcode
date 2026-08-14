class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = {}

        for ch in s:
            if ch in cnt:
                cnt[ch] += 1
            else:
                cnt[ch] = 1
        
        for i, ch in enumerate(s):
            if cnt[ch] == 1:
                return i
        
        return -1