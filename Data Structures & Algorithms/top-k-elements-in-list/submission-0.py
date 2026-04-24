class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key, val in count.items():
            arr[val].append(key)
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if (len(res) == k):
                    return res
        return []