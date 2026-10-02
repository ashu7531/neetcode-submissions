class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        appended = set()
        for i in range(len(strs)):
            if i not in appended:
                appended.add(i)
                anagrams = [strs[i]]
                for j in range(i+1, len(strs)):
                    if j not in appended and self.checkAnagram(strs[i], strs[j]):
                        appended.add(j)
                        anagrams.append(strs[j])
                res.append(anagrams)
        return res
    def checkAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False
        lst = [0] * 26
        for i in range(len(s1)):
            s1_idx = ord(s1[i]) - ord('a')
            lst[s1_idx] += 1
            s2_idx = ord(s2[i]) - ord('a')
            lst[s2_idx] -= 1
        for val in lst:
            if val != 0:
                return False
        return True
