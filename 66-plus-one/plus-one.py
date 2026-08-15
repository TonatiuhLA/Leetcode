class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ""

        for ch in digits:
            st = st + str(ch)
        
        nt = int(st)
        nt += 1

        st = str(nt)
        arr = []

        for ch in st:
            arr.append(int(ch))

        return arr

