from typing import List, Set, Tuple

class Node:
    def __init__(self):
        self.child: dict[str, Node] = {}
        self.end: bool = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def search(self, word: str):
        node = self.root
        for char in word:
            if char in node.child:
                node = node.child[char]
            else:
                return False
        return node.end
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char in node.child:
                node = node.child[char]
            else:
                node.child[char] = Node()
                node = node.child[char]
        node.end = True
    
    def startsWith(self, word: str):
        node = self.root
        for char in word:
            if char in node.child:
                node = node.child[char]
            else:
                return False
        return True
    

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         def find_position_of_starting_word(char:str)-> Set[Tuple[int, int]]:
#             rows, cols = len(board), len(board[0])
#             ans = set()
#             for row in range(rows):
#                 for col in range(cols):
#                     if board[row][col] == char:
#                         ans.add((row, col))
#             return ans
        
#         def is_path_possible(position: Tuple[int, int], ind, word: str, visited_positions: Set[Tuple[int, int]]) -> bool:
#             if ind==len(word):
#                 return True
#             possible_moves = [(-1,0), (1,0), (0,-1), (0,1)]
#             for curr_move in possible_moves:
#                 new_pos = (position[0] + curr_move[0], position[1] + curr_move[1])
#                 if (new_pos in visited_positions) or (new_pos[0]<0 or new_pos[0]>=len(board) or (new_pos[1]<0 or new_pos[1]>=len(board[0]))):
#                     continue
#                 if word[ind] == board[new_pos[0]][new_pos[1]]:
#                     new_position = (new_pos[0], new_pos[1])
#                     visited_positions.add(new_position)
#                     if is_path_possible(new_position, ind+1, word, visited_positions):
#                         return True
#                     visited_positions.remove(new_position)
#             return False
        
#         ans = []
#         for word in words:
#             starting_positions = find_position_of_starting_word(word[0])
#             visited_positions = set()
#             for position in starting_positions:
#                 visited_positions.add(position)
#                 if is_path_possible(position,1, word, visited_positions):
#                     ans.append(word)
#                     break
#                 visited_positions.remove(position)
#         print(board, words)
#         print(ans)
#         return ans

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        rows, cols = len(board), len(board[0])
        for word in words:
            trie.insert(word)
        ans = set()
        def dfs(position: Tuple[int, int], prefix: str, visited_positions: Set[Tuple[int, int]]):
            if trie.search(prefix):
                ans.add(prefix)
            if trie.startsWith(prefix):
                delta = [(-1,0), (1,0), (0,-1), (0,1)]
                for mov in delta:
                    row, col = position[0] + mov[0], position[1] + mov[1]
                    if (row<0 or row==rows) or (col<0 or col==cols) or (row,col) in visited_positions:
                        continue
                    visited_positions.add((row, col))
                    dfs((row, col), prefix + board[row][col], visited_positions)
                    visited_positions.remove((row, col))
        visited_positions = set()
        for i in range(rows):
            for j in range(cols):
                visited_positions.add((i, j))
                dfs((i, j), board[i][j], visited_positions)
                visited_positions.remove((i, j))
        return list(ans)