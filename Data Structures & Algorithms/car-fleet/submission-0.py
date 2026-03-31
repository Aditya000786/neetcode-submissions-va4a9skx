class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = {}
        for i in range(len(position)):
            ps[position[i]] = speed[i]

        position.sort()
        for i in range(len(position)):
            speed[i] = ps[position[i]] 


        time = [None]*len(position)
        for i in range(len(time)):
            time[i] = (target - position[i]) / speed[i]
        stack = [time[-1]]
        for i in range(len(time)-2,-1,-1):
            if time[i]<stack[-1]:
                stack.append(stack[-1])
            else:
                stack.append(time[i])
        ans = 1
        for i in range(1, len(stack)):
            if stack[i]==stack[i-1]:
                continue
            ans+=1
        print(position)
        print(speed)
        print(time)
        print(stack)
        return ans
