class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * (n+2)
        dp2 = [0] * (n+2)
        if (n <= 2):
            return max(nums)
        for i in range(1, n):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
        for i in range(n-1):
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
        return max(dp1[n-1], dp2[n-2])