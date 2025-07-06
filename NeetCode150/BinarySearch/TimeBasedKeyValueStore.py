class TimeMap:

    def __init__(self):
        self.d = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        # O(1)
        if key in self.d:
            self.d[key].append((value, timestamp))
        else:
            self.d[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        xs = self.d.get(key, [])
        res = ""
        l, r = 0, len(xs) - 1

        while l <= r:
            m = (l + r) // 2
            if xs[m][1] <= timestamp:
                res = xs[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

