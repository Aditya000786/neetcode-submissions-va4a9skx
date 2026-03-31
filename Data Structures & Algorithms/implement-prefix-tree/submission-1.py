class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        i=0
        curr = self.root
        while i<len(word):
            next = curr.children.get(word[i])
            if not next:
                curr.children[word[i]] = TrieNode()
                next = curr.children[word[i]]
            curr = next
            i+=1
        curr.is_end = True


    def search(self, word: str) -> bool:
        i=0
        curr = self.root
        while i<len(word):
            next = curr.children.get(word[i])
            if not next:
                return False
            curr = next
            i+=1
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        i=0
        curr = self.root
        while i<len(prefix):
            next = curr.children.get(prefix[i])
            if not next:
                return False
            curr = next
            i+=1
        return True
        
        