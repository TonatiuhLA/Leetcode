class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = ""
        strs.sort()

        if strs:
            for i, ch in enumerate(strs[0]):
                tru = True
                for s in strs:
                    if s[i] != ch:
                        tru = False
                
                if tru:
                    st = st + ch
                else:
                    return st

        return st