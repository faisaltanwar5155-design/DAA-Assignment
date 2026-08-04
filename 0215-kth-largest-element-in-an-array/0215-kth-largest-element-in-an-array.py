class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        new_list = list(sorted(nums))
        length = len(nums) - k
        return new_list[length]