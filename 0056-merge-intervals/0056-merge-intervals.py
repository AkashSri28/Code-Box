class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        for i in range(0,len(intervals)):
            j = i+1
            while j<len(intervals) and intervals[j][0]<=intervals[i][1]:
                intervals[i][1] = max(intervals[i][1],intervals[j][1])
                intervals.pop(j)
        return intervals
        