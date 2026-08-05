class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = float('-inf')
        curr = 0
        for val in nums:
            if curr < 0:
                curr = 0
            curr += val
            if curr > maximum:
                maximum = curr
        return maximum