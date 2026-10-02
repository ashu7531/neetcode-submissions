class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort candidates to handle duplicates
        
        def dfs(total, subset, i):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # Include the current number
            subset.append(candidates[i])
            dfs(total + candidates[i], subset, i + 1)
            subset.pop()
            
            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # Exclude the current number and move to the next unique one
            dfs(total, subset, i + 1)
        
        dfs(0, [], 0)
        return res
