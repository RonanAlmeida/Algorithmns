# Two Number Sum Problem

# Naive Solution
# O(n^2) time, O(1) Space
def two_sum(array,target):
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if array[i]+array[j]==target and i!=j:
                return[array[i],array[j]]
    return []

# O(n) time, O(n) space
# Using Hashmap
def two_sum2(arr,target):
    nums={}
    for num in arr:
        y=target-num
        if y in nums:
            return[y,num]
        else:
            print(nums)
            nums[num]=True
    return[]

# Thrid Solution 
# O(nlogn), space o(1)
def two_sum3(array,targetSum):
    array.sort()
    left =0
    right= len(array)-1
    for num in array:
        if array[left]+array[right]==targetSum:
            return[array[left],array[right]]
        elif array[left]+array[right]>targetSum:
            right-=1
        elif array[left]+array[right]<targetSum:
            left+=1
        print(left)
        print(right)

        
    return[]

def moveElementToEnd(array, toMove):
	# Write your code here.		
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]   
            left+=1
            right-=1
            print('swap')
        if array[left] == toMove and array[right] == toMove:
            right-=1
            
        if array[left] != toMove and array[right] != toMove:
            left+=1
        print(left,right)
        
    return array

if __name__ == "__main__":
    print(moveElementToEnd([1,2,3,2,4,4,2],2))
    # print(two_sum([3,5,-4,8,11,1,-1,6],10))
    # print()
    # print(two_sum2([3,5,-4,8,11,1,-1,6],10))
    # print()
    # print(two_sum3([-1,-2,-3,-4,5,10,15],6))
