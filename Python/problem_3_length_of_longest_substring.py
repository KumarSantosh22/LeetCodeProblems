class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_set = set()
        max_len = 0
        l = 0

        for r in range(len(s)):
            while s[r] in substr_set:
                substr_set.remove(s[l])
                l += 1
            substr_set.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len


# driver code
test_cases = ['abcabcbb', 'bbbbb', 'pwwkew', '', ' ', 'a', 'au']
sol = Solution()

for test in test_cases:
    print(sol.lengthOfLongestSubstring(test))
