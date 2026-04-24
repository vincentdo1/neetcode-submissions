class Solution:
    def findMin(self, nums: List[int]) -> int:
        # for i in range(len(nums) - 1):
        #     if nums[i] <= nums[i + 1]:
        #         continue
        #     else:
        #         return nums[i+1]
        # return nums[0]
        return self.findMinRecursive(nums, 0, len(nums) - 1)
    def findMinRecursive(self, nums, l, r):
        if l == r:
            return nums[l]
        m = l + (r - l) // 2
        if nums[m] < nums[r]:
            return self.findMinRecursive(nums, l, m)
        else:
            return self.findMinRecursive(nums, m + 1, r)
            