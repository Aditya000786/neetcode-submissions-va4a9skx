import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = {}
        for task in tasks:
            if task not in task_map:
                task_map[task] = 0
            task_map[task]+=1
        print(task_map)

        ready = []
        for task, count in task_map.items():
            ready.append((-count, task))
        heapq.heapify(ready)
        print("ready", ready)
        print("task_map", task_map)

        queue = deque([])
        cycle = 0
        while ready or queue:
            # print(ready,queue,cycle)
            cycle+=1
            while queue and queue[0][0]<=cycle:
                ready_time, task, task_count = queue[0]
                heapq.heappush(ready, (-task_count, task))
                queue.popleft()

            if ready:
                new_task_count, new_task = heapq.heappop(ready)
                new_task_count *= -1
                new_task_count -= 1
                if new_task_count>0:
                    queue.append((cycle + n + 1, new_task, new_task_count))
        return cycle

