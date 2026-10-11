class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(1, 33):
            res = res << 1
            res = res | (n & 1)
            n = n >> 1
        return res

        