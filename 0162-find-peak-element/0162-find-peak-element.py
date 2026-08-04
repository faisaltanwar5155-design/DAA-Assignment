class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if l==r:
                return l
            if nums[mid]>nums[mid+1]:
                r = mid
            else:
                l = mid+1