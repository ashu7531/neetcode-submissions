class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0 
        window = len(s) - 1
        
        while window >= 0:
            start = 0
            end = start + window
            while end < len(s):
                substr = s[start: end+1]
                store = set()
                for char in substr:
                    if char in store:
                        break
                    else:
                        store.add(char)
                if len(store) == len(substr):
                    return len(substr)
                else:
                    start += 1
                    end += 1
            window -= 1
                    
        