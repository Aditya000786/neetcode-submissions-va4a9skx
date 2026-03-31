class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mer = sorted(zip(position, speed))
        time = [(target-position)/speed for position, speed in mer]
        stack = []
        for t in time:
            while stack and stack[-1]<=t:
                stack.pop()
            stack.append(t)
        return len(stack)