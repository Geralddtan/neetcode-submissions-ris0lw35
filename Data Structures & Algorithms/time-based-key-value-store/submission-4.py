class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        substore = self.store[key]
        if not substore:
            return ""
        # Binary Search
        l, r = 0, len(substore)-1
        while l <= r:
            mid = (l+r)//2
            if timestamp > substore[mid][1]:
                l = mid+1
            elif timestamp < substore[mid][1]:
                r = mid-1
            else:
                return substore[mid][0]
        
        if timestamp > substore[mid][1]:
            return substore[mid][0]
        elif timestamp < substore[mid][1] and mid > 0:
            return substore[mid-1][0]
        else:
            return ""
    
