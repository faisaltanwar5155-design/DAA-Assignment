class Solution(object):
    def sortArray(self, nums):
        def mergeSort(nums,left,right,mid):
            i = left
            j = mid+1
            temp = []
            while i<=mid and j<=right:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while i<=mid:
                temp.append(nums[i])
                i+=1
            while j<=right:
                temp.append(nums[j])
                j+=1
            for k in range(len(temp)):
                nums[left+k] = temp[k]
        def merge(nums,left,right):
            if left<right:
                mid = left +(right-left)//2
                merge(nums,left,mid)
                merge(nums,mid+1,right)
                mergeSort(nums,left,right,mid)        
        merge(nums,0,len(nums)-1)
        return nums