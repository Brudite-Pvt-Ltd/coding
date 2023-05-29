class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        r = []
        intervals.sort()
        for intervals in intervals:
            if r == []:
                r.append(intervals)
            elif r[-1][1] < intervals[0]:
                r.append(intervals)
            else:
                r[-1][1] = max(r[-1][1],intervals[1])
        return r
    

