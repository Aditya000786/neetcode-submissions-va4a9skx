class TrieNode:
    def __init__(self):
        self.edges = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.edges:
                curr.edges[c] = TrieNode()
            curr = curr.edges[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            # if len(word) == 0: 
            #     if len(node.edges):
            #         return False
            #     return True
            for i in range(len(word)):
                if word[i] == ".":
                    found = False
                    if i+1==len(word):
                        for e in node.edges:
                            if node.edges[e].endOfWord:
                                found = True
                    else:
                        for e in node.edges:
                            if dfs(node.edges[e], word[i+1:]):
                                found = True
                                break
                    if not found:
                        return False
                    else:
                        return True
                else:
                    if word[i] not in node.edges:
                        return False
                    node = node.edges[word[i]]
            return node.endOfWord
        return dfs(self.root, word)