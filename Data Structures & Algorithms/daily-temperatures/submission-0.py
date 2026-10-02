class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            numdays = 0
            for j in range(i+1, len(temperatures)):
                numdays += 1
                if temperatures[j] > temperatures[i]:
                    break
                if (j == len(temperatures) - 1) and temperatures[j] <= temperatures[i]:
                    numdays = 0
            res.append(numdays)
        return res
