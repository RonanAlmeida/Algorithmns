

def binary_search(array,target):
    array.sort()
    left = 0
    right = len(array)-1

    while left<=right:
        mid = (left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]