class Solution(object):
    # Accepted O(2n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = i = j = 0
        substringDic = {}
        stringLen = len(s)
        while i < stringLen and j < stringLen:
            if s[j] in substringDic:
                answer = max(answer, j - i)
                del substringDic[s[i]]
                i = i + 1
            else:
                substringDic[s[j]] = j
                j = j + 1

        return max(answer, j - i)

# Accepted O(n) better
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = i = 0
        substringDic = {}
        for j in range(0, len(s)):
            if s[j] in substringDic and substringDic[s[j]] >= i:
                # TODO: is line seems necessary, but actually not, thing about it
                # answer = max(answer, j - i)
                i = substringDic[s[j]] + 1
            else:
                substringDic[s[j]] = j
                answer = max(answer, j - i + 1)
            substringDic[s[j]] = j
        return answer




print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution2().lengthOfLongestSubstring("abcabcbb")