class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start=0
        count=0
        for end in range(1,len(s)+1):
            if len(set(s[start:end]))==len(s[start:end]):
                if (end-start+1)>count:
                    count=len(s[start:end])
            else:
                start+=1
        return(count)