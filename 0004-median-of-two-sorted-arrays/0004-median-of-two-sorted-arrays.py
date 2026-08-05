class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        l = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        while j<len(nums2):
            l.append(nums2[j])
            j+=1
        while i<len(nums1):
            l.append(nums1[i])
            i+=1
        n = len(l)
        if n%2==0:
            return (l[n//2]+l[n//2 - 1])/2.0
        else:
            return l[n//2]
        