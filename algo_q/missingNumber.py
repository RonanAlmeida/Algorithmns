class Solution(object):
    # O(n) time and space 
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap={}
        for num in nums:
            if num not in hashMap:
                hashMap[num]=True
        
        for i in range(0,len(nums)+1):
            if i not in hashMap:
                return i