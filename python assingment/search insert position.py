class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        while start != end:
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        return start
