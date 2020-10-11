# array that stores previous 2 fibs
# o(n) time o(1) space
def getNthFib(n):

        if n==1:
            return 0
        if n==2:
            return 1
        fibSum=0
        prevTerms=[0,1] # fib(n-1) + fib(n-2)
        for i in range(2,n+1):	
            # print(i)
            # if i>2:
                fibSum=prevTerms[0]+prevTerms[1]
                prevTerms[1] = prevTerms[0] 
                prevTerms[0]=fibSum
                print(prevTerms)
                # print(fibSum)

        return fibSum


	# 1 [0,1] -> 0
	# 2 [0,1] -> 1
	# 3 [1,1] -> 1
	# 4 [2,1] -> 2
	# 5 [3,2]
	# 6 [5,3]
	# FIB-> 0 1 1 2 3 5 8 13
	# N---> 1 2 3 4 5 6 7 8
if __name__ == "__main__":
    print(getNthFib(8))
    # print(getNthFib(2))