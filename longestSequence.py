class Solution:
    def longestSubsequence(self, arr, difference: int):

        mp = defaultdict(int)
        mx=0
        for i in arr:
            mp[i]=mp[i-difference]+1
            mx=max(mp[i],mx)
        return mx