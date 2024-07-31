class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis={
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack=[]
        
        for i in s:
            if i in paranthesis.values():
                stack.append(i)
            elif i in paranthesis and stack and stack[-1 ]==paranthesis[i]:
                stack.pop()
            else:
                return False
        return not stack
