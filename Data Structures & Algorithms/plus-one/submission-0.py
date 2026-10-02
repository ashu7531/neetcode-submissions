class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        res = []
        carry = 1
        while carry and pointer >= 0:
            sum_val = digits[pointer] + carry
            carry = sum_val // 10
            sum_val = sum_val % 10
            res.append(sum_val)
            pointer -= 1
        if carry:
            res.append(carry)
        while pointer >= 0:
            res.append(digits[pointer])
            pointer -= 1
        return res[::-1]
        