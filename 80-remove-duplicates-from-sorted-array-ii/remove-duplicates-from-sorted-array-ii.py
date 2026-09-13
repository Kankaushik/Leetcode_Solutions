class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        j=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                    k +=1
            else:
                k=1

            if k <=2:
                nums[j] = nums[i]
                j +=1
                    
        return j
        