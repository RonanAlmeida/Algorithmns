# Two Number Sum

# Naive Solution
# O(n^2)
def two_sum(array,target):
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if array[i]+array[j]==target and i!=j:
                return[array[i],array[j]]
    return []

# O(n)
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

if __name__ == "__main__":
    print(two_sum([3,5,-4,8,11,1,-1,6],10))
    print(two_sum2([3,5,-4,8,11,1,-1,6],10))
    