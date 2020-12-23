def findThreeLargestNumbers(array):
	largest=[array[0],array[1],array[2]]
	s=array.sort()
	print(s[0])
	# if len(array)==3:
		# print("hey")

	for num in array:
		if num>=largest[2]:
			largest[0]=largest[1]
			largest[1]=largest[2]
			largest[2]=num
		
		elif num>=largest[1]:
			largest[0]=largest[1]
			largest[1]=num

		elif num>=largest[0]:
			largest[0]=num
		
	return largest
		
print(findThreeLargestNumbers([7,8,55]))