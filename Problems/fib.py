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

def printthis(n):
    # odd 
    # 5 4 3 2 1
    # 5  AAAAA
    # 3  0AAA4    5 3 
    # 1  01A34    5 1 0 1 2 3 4 


    # AAAAAAA
    # 0AAAAA1
    #   AAA
    #    A  01234
    if n%2!=0:
        nMAX=n
        nSub =n
        listN=['']*nMAX
        while (nSub>0):

            if (nSub%2!=0):
                diff = nMAX-nSub
                string = 'A'*nSub
                spaces = diff 

                
                
            nSub-=1
    

if __name__ == "__main__":

    print(printthis(5))
    # print(getNthFib(2))