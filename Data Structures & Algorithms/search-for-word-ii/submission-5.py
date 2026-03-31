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

    def searchWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char] 
        return curr.endOfWord

    def startsWith(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char] 
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie: Trie = Trie()
        for word in words:
            trie.addWord(word)
        
        # visited = set()
        # curr_word = ""
        ans = set()

        def traverse(row_ind, col_ind):
            nonlocal curr_word, ans
            char = board[row_ind][col_ind]
            curr_word+=char
            # print("start traverse", row_ind, col_ind, curr_word)

            if trie.searchWord(curr_word):
                # print("searchWord")
                ans.add(curr_word)

            if trie.startsWith(curr_word):
                # print("startsWith")
                for delta_row, delta_col in [(-1,0), (1,0), (0,-1), (0,1)]:
                    new_row, new_col = row_ind + delta_row, col_ind + delta_col
                    if (new_row <0 or new_row>=len(board) or 
                        new_col<0 or new_col>=len(board[0]) or (new_row, new_col) in visited):
                        continue
                    else:
                        visited.add((new_row, new_col))
                        
                        # char = words[row_ind][col_ind]
                        # curr_word+=char
                        
                        traverse(new_row, new_col)

                        visited.remove((new_row, new_col))
            
            curr_word=curr_word[:-1]
            # print("end traverse", row_ind, col_ind, curr_word)

        for row in range(len(board)):
            for col in range(len(board[0])):
                visited = set()
                visited.add((row, col))
                curr_word = ""
                # ans = set()
                traverse(row, col)

        a = list(ans)
        return a

        