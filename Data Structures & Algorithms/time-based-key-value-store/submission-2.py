class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map.setdefault(key, []).append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hash_map:
            return ""
        values = self.hash_map[key]
        low, high = 0, len(values)-1
        ans = (float('-inf'), "")
        print(values)
        while low<=high:
            mid = (low + high)//2
            print(low, high, mid)
            if values[mid][0] <= timestamp:
                if ans[0]<values[mid][0]:
                    ans = values[mid]
                low = mid+1
            else:
                high = mid-1
        return ans[-1]