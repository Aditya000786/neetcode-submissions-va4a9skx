class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = 1
        close = 0
        result = []
        def backtrack(current:str, open_count:int, close_count: int):
            if len(current) == 2*n:
                result.append(current)
            else:
                if open_count<n:
                    backtrack(current+"(", open_count+1, close_count)
                if close_count<open_count:
                    backtrack(current+")", open_count, close_count+1)
        backtrack("", 0, 0)  
        return result              
    