class Solution:
    def longestSubsequence(self, arr, difference: int):

        mp = defaultdict(int)
        mx=0
        for i in arr:
            mp[i]=mp[i-difference]+1
            mx=max(mp[i],mx)
        return mx



def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])

            res = max(res, r - l + 1)

        return res