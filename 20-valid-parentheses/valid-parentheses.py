class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen={"}":"{",
        "]":"[",
        ")":"("}
        for c in s:
            if c in "[{(":
                stack.append(c)
            else:
                if len(stack)==0 or stack[-1]!=closeToOpen[c]:
                    return False
                else:
                    stack.pop()
        return True if len(stack)==0 else False



 
        
        
        