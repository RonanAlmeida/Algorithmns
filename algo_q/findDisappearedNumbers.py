class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        O(n) time and space 

        """
        hashMap={}
        for num in nums:
            hashMap[num]=True
            
        missing=[]
        for i in range(1,len(nums)+1):
            if i not in hashMap:
                missing.append(i)
        return missing

    def findDisappearedNumbersOptimal(self,nums):
