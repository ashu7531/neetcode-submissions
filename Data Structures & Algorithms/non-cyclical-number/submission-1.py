class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        
        
        while n not in results and n != 1:
            results.add(n)
            n = self.sumSquareofDigits(n)
            
        if n == 1:
            return True
        return False
        
    def sumSquareofDigits(self, nums):
        sum_val = 0
        while nums:
            res = nums % 10
            res = res * res
            sum_val += res
            nums = nums // 10
        return sum_val


        