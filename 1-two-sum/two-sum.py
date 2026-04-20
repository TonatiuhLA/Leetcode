class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, j in enumerate(nums):
            num = target - j
            if num in seen:
                return [seen[num], i]
            seen[j] = i
        