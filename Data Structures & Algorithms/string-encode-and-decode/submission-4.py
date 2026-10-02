class Solution:

    def encode(self, strs: List[str]) -> str:
        # we need to add num
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            curr = i
            while s[i] != "#":
                i += 1
            count = int(s[curr:i])
            res.append(s[i+1: i + count + 1])
            i = i + count + 1
        return res
