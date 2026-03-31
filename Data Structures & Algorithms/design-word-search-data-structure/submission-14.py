class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        
class WordDictionary:

    def __init__(self):
        self.root  = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        i = 0
        while i < len(word):
            next = curr.children.get(word[i])
            if not next:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
            i+=1
        curr.word = True
        

    def search(self, word: str) -> bool:
        def search_with_node(word:str, node: TrieNode):
            if len(word) == 0:
                if not node or len(node.children.keys())==0:
                    return True
                else:
                    return False
            curr = node
            i = 0
            while i < len(word):
                if word[i] == ".":
                    for child in curr.children:
                        if search_with_node(word[i+1:], curr.children[child]):
                            return True
                    return False
                else:
                    next = curr.children.get(word[i])
                    if not next:
                        return False
                    curr = next
                i+=1
            return True
        return search_with_node(word, self.root)


        
