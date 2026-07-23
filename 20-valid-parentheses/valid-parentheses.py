class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if self.isOpen(ch):
                stack.append(ch)
            else:
                if len(stack) > 0:
                    curr = stack.pop()
                    if b_map[ch] != curr:
                        return False
                else:
                    return False
        
        if len(stack) > 0:
            return False
        return True
    
    def isOpen(self, s) -> bool:
        if s == '(' or s == '{' or s == '[':
            return True
        return False