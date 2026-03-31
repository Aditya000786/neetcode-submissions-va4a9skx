class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.endOfWord = True
    
    def search(self, word):
        curr = self.root
        for w in word:
            if w not in curr.child:
                return False, False
            curr = curr.child[w]
        return True, curr.endOfWord
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for ind in range(len(words)):
            t.insert(words[ind])

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        ans = set()
        def dfs(row, col, node, pre_word):
            if (row<0 or col<0 or row == ROWS or col == COLS 
            or (row, col) in visited 
            or board[row][col] not in node.child):
                return
            visited.add((row, col))
            node = node.child[board[row][col]]
            word = pre_word + board[row][col]
            if node.endOfWord:
                ans.add(word)

            direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for di in direc:
                nr, nc = di[0]+row, di[1]+col
                dfs(nr, nc, node, word)

            visited.remove((row, col))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, t.root, "")
        return list(ans)



        