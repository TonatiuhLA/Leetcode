class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        front = 0
        back = len(s) - 1
        while front < back:
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1
        
        return True