class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n

        while num != 1:
            st = str(num)
            num = 0
            for d in st:
                curr = int(d)
                num += curr * curr
            
            if num in seen:
                return False

            seen.add(num)

        return True