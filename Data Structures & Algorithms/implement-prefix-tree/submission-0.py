class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

        
    def insert(self, word: str) -> None:
        curr_node: TrieNode = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr_node: TrieNode = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True if curr_node.end_of_word else False

    def startsWith(self, prefix: str) -> tuple[TrieNode, bool]:
        curr_node: TrieNode = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True