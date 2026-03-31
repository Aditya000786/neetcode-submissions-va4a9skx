class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for ind in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[ind]:
                pop_ind = stack.pop()
                res[pop_ind] = ind-pop_ind
            stack.append(ind)
        return res