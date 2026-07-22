class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        length = len(s) - 1

        if length == 0:
            total += values[s[0]]
        else:
            for i in range (0, length):
                if values[s[i]] < values[s[i+1]]:
                    total -= values[s[i]]
                else:
                    total += values[s[i]]
            
            total += values[s[length]]
        return total
