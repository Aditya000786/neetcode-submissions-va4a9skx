class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hash_map[key]
        low, high = 0, len(values)-1
        res = ""
        while low<=high:
            mid = (low+high)//2
            if values[mid][0]>timestamp:
                high = mid-1
            else:
                res = values[mid][1]
                low = mid+1
        return res