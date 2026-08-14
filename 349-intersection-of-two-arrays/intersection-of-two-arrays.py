class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        arr = []

        for i in nums1:
            if i not in seen:
                seen.add(i)
        
        for i in nums2:
            if i in seen and i not in arr:
                arr.append(i)
        
        return arr