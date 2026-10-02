class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '[]'
        encoded = '{|}'.join(strs)
        return encoded


    def decode(self, s: str) -> List[str]:
        if s == '[]':
            return []
        decoded = s.split('{|}')
        return decoded