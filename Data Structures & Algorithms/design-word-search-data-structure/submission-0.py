class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.endofword = True
        

    def search(self, word: str) -> bool:
        def dfs(node, ind):
            if ind == len(word):
                return node.endofword
            letter = word[ind]
            if letter == ".":
                for child in node.children.values():
                    if dfs(child, ind + 1):
                        return True
                return False

            if letter not in node.children:
                return False
            return dfs(node.children[letter], ind + 1)
        return dfs(self.root, 0)
            

#     r -> b - a - d
#     r -> d - a - d
#     r -> m - a - d

# root - > {TrieNode(b, false), }
#   


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)