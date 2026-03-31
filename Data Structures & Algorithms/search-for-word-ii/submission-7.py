class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.addWord(word)

        ans = set()
        ROWS, COLS = len(board), len(board[0])

        def traverse(r, c, node, curr_word):
            char = board[r][c]

            if char not in node.children:
                return  # no prefix → prune immediately

            node = node.children[char]
            curr_word += char

            if node.endOfWord:
                ans.add(curr_word)

            visited.add((r, c))

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    traverse(nr, nc, node, curr_word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                traverse(r, c, trie.root, "")

        return list(ans)
