class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        s = []
        for i in nums:
            if i == 1:
                k+=1
            else:
                s.append(k)
                k = 0
            s.append(k)
        return max(s)
            
