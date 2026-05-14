class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = max(nums) + 1
        freq = {}
        for num in nums:
            if (num not in freq):
                freq[num] = 0
            else:
                freq[num] += 1
        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        res = []
        for key, value in sorted_dict.items():
            res.append(key)
            k -= 1
            if (k == 0):
                break
        return res