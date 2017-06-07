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
        parts = toMergedPart, firstPart, lastPart = [],[],[]
        mergedInterval = newInterval

        for item in intervals:
            if item.start > newInterval.end:
                lastPart.append(item)
            elif item.end < newInterval.start:
                firstPart.append(item)
            else:
                toMergedPart.append(item)

        # concise, however a little bit tricky way. Equals the for loop before
        # for item in intervals:
        #     parts[(item.end < newInterval.start) - (item.start > newInterval.end)].append(item)

        if toMergedPart:
            mergedInterval = Interval(min(toMergedPart[0].start, newInterval.start), max(toMergedPart[-1].end, newInterval.end))

        return firstPart + [mergedInterval] + lastPart

result = Solution().insert([Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)],Interval(4,9))
