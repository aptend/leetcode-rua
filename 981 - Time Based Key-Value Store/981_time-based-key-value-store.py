from collections import namedtuple
from bisect import bisect_right
serial = namedtuple('serial', 'vals timestamps')

class TimeMap:
    # 612ms 90.84% / 628ms / 640ms
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.data:
            self.data[key] = serial([value], [timestamp])
            return
        self.data[key].timestamps.append(timestamp)
        self.data[key].vals.append(value)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.data:
            return ""
        d = self.data[key]
        idx = bisect_right(d.timestamps, timestamp)
        if idx == 0:
            return ""
        else:
            return d.vals[idx-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
def main():
    timemap = TimeMap()
    operations = ['TimeMap', 'set', 'get', 'get', 'set', 'get', 'get']
    operands = [[], ['foo', 'bar', 1], ['foo', 1], ['foo', 3], ['foo', 'bar2', 4], ['foo', 4], ['foo', 5]]
    for opt, opd in zip(operations, operands):
        if hasattr(timemap, opt):
            print(getattr(timemap, opt).__call__(*opd))


if __name__ == "__main__":
    main()
