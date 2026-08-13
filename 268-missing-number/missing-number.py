class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        seen = set()

        for num in nums:
            seen.add(num)
        
        for i in range(leng+1):
            if i not in seen:
                return i
        