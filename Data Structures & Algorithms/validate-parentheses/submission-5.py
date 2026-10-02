class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap  = { '}':'{', ')':'(' , ']':'[' }
        for i in s:
            if i in hashmap.values():
                stack.append(i)
            elif i in hashmap.keys():
                if not stack or stack.pop() != hashmap[i]:
                    return False
        return not stack


