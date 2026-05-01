class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if (n <= 2):
            return max(nums)
        first = [0] * (n)
        last = [0] * (n)
        first[0] = nums[0]
        first[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            first[i] = max(first[i - 2] + nums[i], first[i - 1])

        last[1] = nums[1]
        last[2] = max(nums[1], nums[2])
        for i in range(3, n):
            last[i] = max(last[i - 2] + nums[i], last[i - 1])
        return max(last[n-1], first[n-2])