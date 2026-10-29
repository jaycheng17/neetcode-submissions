class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for character in s:
            if character in pairs:
                if stack and stack[-1] == pairs[character]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(character)

        return True if not stack else False
                