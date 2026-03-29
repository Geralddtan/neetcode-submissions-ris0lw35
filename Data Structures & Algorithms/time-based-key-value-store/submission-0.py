class TimeMap:

    def __init__(self):
        self.keystore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.keystore[key]
        
        l,r=0,len(values)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if values[mid][1] > timestamp:
                r = mid - 1
            else:
                res = values[mid][0]
                l = mid + 1

        return res

