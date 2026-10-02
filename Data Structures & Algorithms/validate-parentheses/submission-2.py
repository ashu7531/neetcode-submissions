class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(' : ')', '{' : '}', '[' : ']'}
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                curr_bracket = stack.pop()
                if brackets[curr_bracket] != bracket:
                    return False
        if len(stack) == 0:
            return True
        return False
                    