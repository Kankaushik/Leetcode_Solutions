class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()
        for i in range(len(nums)):
            if nums[i] in check:
                return True
            check.add(nums[i])
            
            if len(check) > k:
                check.remove(nums[i-k])
        return False