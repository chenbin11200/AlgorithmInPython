class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            nums1 = nums2
        if len(nums2) == 0:
            nums2 = nums1
        i = j = 0
        mark = False
        counter = sum = val = 0
        totalLength = len(nums1) + len(nums2)
        if totalLength % 2 == 0:
            n1 = totalLength / 2 - 1
            mark = judger = True
        else:
            n1 = totalLength / 2
            mark = judger = False
        while i < len(nums1) or j < len(nums2):
            if nums1[i] < nums2[j]:
                val = nums1[i]
                if i < len(nums1) - 1:
                    i = i + 1
                elif j < len(nums2)-1:
                    j = j + 1
            # elif nums1[i]>nums2[j]:nums2[j]
            else:
                val = nums2[j]
                if j < len(nums2) - 1:
                    j = j + 1
                elif i < len(nums1)-1:
                    i = i + 1
            if counter == n1 or counter == n1 + 1:
                sum = sum + val
                if mark:
                    mark = False
                    continue
                else:
                    break
            counter = counter + 1
        if judger:
            return sum / 2
        return sum


class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            nums1 = nums2
        if len(nums2) == 0:
            nums2 = nums1
        i = j = 0
        mark = False
        counter = sum = val = 0
        totalLength = len(nums1) + len(nums2)
        if totalLength % 2 == 0:
            n1 = totalLength / 2 - 1
            mark = judger = True
        else:
            n1 = totalLength / 2
            mark = judger = False

        for finalIndex in range(0, n1+2):
            if i>=len(nums1):
                val = nums2[j]
                j=j+1
            elif j>=len(nums2):
                val = nums1[i]
                i=i+1
            else:
                if nums1[i] < nums2[j]:
                    val = nums1[i]
                    i = i + 1
                else:
                    val = nums2[j]
                    j = j + 1
            if counter == n1 or counter == n1 + 1:
                sum = sum + val
                if mark:
                    mark = False
                    continue
                else:
                    break
            counter = counter + 1
        if judger:
            return sum / 2.0
        return sum

print Solution2().findMedianSortedArrays([1,2],[3,4])