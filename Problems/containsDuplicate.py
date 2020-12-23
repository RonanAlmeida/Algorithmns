class Solution(object):
    # O(n) time and space 
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numHash={}
        for num in nums:
            if num in numHash:
                return True
            else:
                numHash[num]=True
        return False
    
