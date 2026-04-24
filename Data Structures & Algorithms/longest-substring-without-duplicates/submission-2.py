class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx, res, l = 0, 0, 0
        set_ = set()
        while (idx < len(s)):
            if (s[idx] not in set_):
                set_.add(s[idx])
                l += 1
                idx += 1
            else:
                set_.clear()
                res = max(res, l)
                idx = idx - l + 1
                l = 0
        return max(res, l)