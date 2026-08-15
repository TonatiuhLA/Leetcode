class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        amt = 0

        while l < r:
            left, right = height[l], height[r]
            sq = min(left, right)
            dst = r - l
            print(sq, dst)
            print()

            if sq * dst > amt:
                amt = sq * dst
            
            if left == right:
                r -= 1
            else:
                if left < right:
                    l += 1
                else:
                    r -= 1
        
        return amt
