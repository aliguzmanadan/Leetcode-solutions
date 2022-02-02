class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for char in s:
            if char in ("(", "{", "["):
                stack.append(char)
            elif not stack:
                return False
            elif  closing_dict[char] != stack[-1]:
                return False
            else:
                stack.pop()
            
        return not stack
    
    
    