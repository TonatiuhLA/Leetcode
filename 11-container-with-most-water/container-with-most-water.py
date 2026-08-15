class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        amt = 0

        while l < r:
            currAmt = min(height[l], height[r]) * (r - l)
            amt = max(amt, currAmt)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return amt
