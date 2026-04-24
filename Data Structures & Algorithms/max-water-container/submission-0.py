class Solution:
    def helper(self, l, r, heights):
        if (l >= r or r > len(heights) or l < 0):
            return 0
        area = (r - l) * min(heights[l], heights[r])
        return max(self.helper(l+1, r, heights), self.helper(l, r-1, heights), area)
    def maxArea(self, heights: List[int]) -> int:
        res = 1
        l = 0
        r = len(heights) - 1
        return self.helper(l, r, heights)