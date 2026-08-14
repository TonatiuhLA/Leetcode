class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = {}
        mag = {}

        for ch in ransomNote:
            if ch not in ran:
                ran[ch] = 1
            else:
                ran[ch] += 1
        
        for ch in magazine:
            if ch not in mag:
                mag[ch] = 1
            else:
                mag[ch] += 1
        
        for ch in ran:
            if ch not in mag or ran[ch] > mag[ch]:
                return False
        
        return True