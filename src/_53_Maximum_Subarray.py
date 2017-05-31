class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        statusArray = list(nums)
        result = nums[0]
        if len(nums) == 1:
            return result
        for i in range(1, len(nums)):
            if statusArray[i - 1] > 0:
                statusArray[i] = statusArray[i-1] + statusArray[i]
            result = max(statusArray[i], result)
        return result

# This is the better solution
class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :return: int
        """
        currentSum = maxSum = nums[0]
        for num in nums[1:] : # In this way, we could avoid using index
            currentSum = max(num, num + currentSum) # equals statusArray[i-1]
            maxSum = max(currentSum, maxSum)
        return maxSum

print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print Solution2().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])