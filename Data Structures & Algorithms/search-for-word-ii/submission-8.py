class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
        self.ind = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, ind):
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.endOfWord = True
        curr.ind = ind
    
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
            t.insert(words[ind], ind)

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        ans = set()
        def dfs(pre_word, row, col):
            if (row, col) in visited:
                return
            visited.add((row, col))
            
            word = pre_word + board[row][col]
            res, isEnd = t.search(word)
            # print("word", word, pre_word, res, isEnd)
            if isEnd:
                ans.add(word)
            if not res:
                visited.remove((row, col))
                return
            direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for di in direc:
                nr, nc = di[0]+row, di[1]+col
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS:
                    continue
                dfs(word, nr, nc)

            visited.remove((row, col))
        for r in range(ROWS):
            for c in range(COLS):
                dfs("", r, c)
        return list(ans)



        