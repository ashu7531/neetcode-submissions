class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = self.prettify(s)
        start = 0
        end = len(new_str) - 1
        while start < end:
            if new_str[start] == new_str[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
    def prettify(self, s):
        new_str = ''
        for char in s:
            if char.isalnum():
                new_str += char.lower()
        return new_str
