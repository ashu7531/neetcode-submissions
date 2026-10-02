class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window = len(s1)
        start = 0
        end = window
        while end <= len(s2):
            new_s2 = s2[start: end]
            ans = self.checkPermutation(s1, new_s2)
            if ans:
                return True
            start += 1
            end += 1
        return False

    def checkPermutation(self, s1, s2):
        charFreq = {chr(c) : 0 for c in range(ord('a'), ord('z') + 1)}
        for char in s2:
            if char in charFreq:
                charFreq[char] += 1
            else:
                charFreq[char] = 0
        for char in s1:
            if char in charFreq:
                charFreq[char] -= 1
            else:
                return False
        for char in charFreq:
            if charFreq[char] != 0:
                return False
        return True
                
        
        