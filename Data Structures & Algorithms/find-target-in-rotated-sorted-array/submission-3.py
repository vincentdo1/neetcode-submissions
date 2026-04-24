class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l+ (r-l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binarySearch(l, r):
            while (l <= r):
                mid = (l + r) // 2
                if (nums[mid] > target):
                    r = mid - 1
                elif (nums[mid] < target):
                    l = mid + 1
                else:
                    return mid
            return -1
        result = binarySearch(0, pivot - 1)
        if result != -1:
            return result
        
        return binarySearch(pivot, len(nums) - 1)