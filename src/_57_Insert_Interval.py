# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        firstPart = [item for item in intervals if item.end < newInterval.start]
        lastPart = [item for item in intervals if item.start > newInterval.end]
        rest = list(set(intervals)^set(firstPart)^set(lastPart))
        middle = newInterval
        if rest:
            left, right = newInterval.start, newInterval.end
            for i in rest:
                left = min(left, i.start)
                right = max(right, i.end)
            middle = Interval(left, right)

        return firstPart + [middle] + lastPart

result = Solution().insert([Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)],Interval(4,9))
