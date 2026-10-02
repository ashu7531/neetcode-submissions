class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach:
        # Make a list of length 26 and fill 0 at each position.
        # Iterate over s and convert char into ord and subtract 97 from that and add 1 to the result list at index num(num is result obtained by subtracting 97 form ord of char).
        # Iterate over t and do the same part of conversion and subtraction and subtract 1 to the result list at index num(num is result obtained by subtracting 97 form ord of char).
        if len(s) != len(t):
            return False
        lst = []
        for i in range(27):
            lst.append(0)
        for char in s:
            idx = ord(char) - 97
            lst[idx] += 1
        for char in t:
            idx = ord(char) - 97
            lst[idx] -= 1
        for i in range(27):
            if lst[i] != 0:
                return False
        return True
        
        