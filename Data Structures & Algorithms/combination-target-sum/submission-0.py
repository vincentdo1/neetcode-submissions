class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(idx: int, total: int, combinations: List[int]):
            if total > target or idx == len(nums):
                return
            if total == target:
                res.append(combinations[:])  # copy
                return

            # take nums[idx]
            combinations.append(nums[idx])
            helper(idx, total + nums[idx], combinations)
            combinations.pop()

            # skip nums[idx]
            helper(idx + 1, total, combinations)

        res = []
        helper(0, 0, [])
        return res