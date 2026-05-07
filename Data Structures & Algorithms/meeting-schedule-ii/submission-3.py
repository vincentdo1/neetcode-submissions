class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        s = e = 0
        rooms = 0
        max_rooms = 0
        n = len(intervals)

        while s < n:
            if starts[s] < ends[e]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1

        return max_rooms