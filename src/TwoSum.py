class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        startIndex = 0
        endIndex = len(sortedNums)-1
        result = []
        while startIndex != endIndex:
            if sortedNums[startIndex]+sortedNums[endIndex]==target:
                break
            elif sortedNums[startIndex]+sortedNums[endIndex]>target:
                endIndex = endIndex - 1
            else:
                startIndex = startIndex + 1
        resultCount = 0
        for index,value in enumerate(nums):
            if value == sortedNums[startIndex] or value == sortedNums[endIndex]:
                result.append(index)
                resultCount = resultCount + 1
            if resultCount == 2:
                return result

class Solution2(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


a = Solution().twoSum([2,5,7,8,9,11,15],9)
print a
b = Solution2().twoSum([2,5,7,8,9,11,15],9)
print b

