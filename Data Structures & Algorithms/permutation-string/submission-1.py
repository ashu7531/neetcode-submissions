class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = {chr(c) : 0 for c in range(ord('a'), ord('z') + 1)}
        for char in s1:
            s1_count[char] += 1
        window_count = {chr(c) : 0 for c in range(ord('a'), ord('z') + 1)}
        for idx in range(len(s1)):
            window_count[s2[idx]] += 1
        for idx in range(len(s2)- len(s1)):
            if s1_count == window_count:
                return True
            window_count[s2[idx]] -= 1
            window_count[s2[idx + len(s1)]] += 1
        return window_count == s1_count

        