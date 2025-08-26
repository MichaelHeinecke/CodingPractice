from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if i == len(intervals) - 1:
                res.append(curr)
                break
            foll = intervals[i + 1]

            # If foll start before curr end, they overlap
            if foll[0] <= curr[1]:
                foll[0] = curr[0]
                # Take larger end time
                foll[1] = max(curr[1], foll[1])
            else:
                res.append(curr)

        return res

if __name__ == '__main__':

    i = [[1,4],[4,6],[8,10],[15,18]]
    print(Solution().merge(i))
