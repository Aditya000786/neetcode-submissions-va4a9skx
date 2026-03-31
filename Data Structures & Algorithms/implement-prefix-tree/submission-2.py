class TrieNode:
    def __init__(self):
        self.isWord = False
        self.edges = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.edges:
                curr.edges[w] = TrieNode()
            curr = curr.edges[w]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.edges:
                return False
            curr = curr.edges[w]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.edges:
                return False
            curr = curr.edges[w]
        return True
        