class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ptr = 0
        st = ""
        arr = []

        while ptr < len(s):
            if s[ptr] != " ":
                st = st + s[ptr]
            else:
                arr.append(st)
                st = ""
            ptr += 1
        arr.append(st)

        if len(arr) > len(pattern) or len(pattern) > len(arr):
            return False

        char_to = {}
        word_to = {}

        for i, c in enumerate(pattern):
            if c in char_to:
                if char_to[c] != arr[i]:
                    return False
            elif arr[i] in word_to:
                if word_to[arr[i]] != c:
                    return False
            else:
                char_to[c] = arr[i]
                word_to[arr[i]] = c
            

        return True            