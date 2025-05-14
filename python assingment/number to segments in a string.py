class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = s.split(" ")
        count = 0
        for x in list1:
            if x =="":
                count += 1      
        segment = len(list1) - count
        return segment
