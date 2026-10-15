class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in closed_to_open:
                if not stack or closed_to_open[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
                
