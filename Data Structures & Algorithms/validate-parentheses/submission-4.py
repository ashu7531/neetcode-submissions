class Solution:
    def isValid(self, s: str) -> bool:
        # example:
        # 1. [{()}], true
        # 2. [{]}, false
        # 3. null
        # sol:
        # 1. store bracket in stack if open else pop
        # 2. check popped value with the correspondvalue of current bracket 
        # 3. repeat this process of checking and popping till end
        # Test cases:
        # 1. [{}]()(), true
        # 2. []{})(, false
        # 3. ]})

        # code:
        stack = []
        dictionary = {'(' : ')', '{' : '}', '[' : ']'}
        for bracket in s:
            if bracket in dictionary:
                stack.append(bracket)
            else:
                if not len(stack) == 0:
                    curr_bracket = stack.pop()
                    if curr_bracket == '(':
                        if dictionary[curr_bracket] != bracket:
                            return False
                    if curr_bracket == '{':
                        if dictionary[curr_bracket] != bracket:
                            return False
                    if curr_bracket == '[':
                        if dictionary[curr_bracket] != bracket:
                            return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        # validation:

        
                

