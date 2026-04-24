"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
""" 

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda i: i.start)
        curr_max = -1
        for interval in intervals:
            if (curr_max > interval.start):
                return False
            curr_max = max(curr_max, interval.end)
        return True
