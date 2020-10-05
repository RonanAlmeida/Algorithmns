# O(n) time, O(n) space
def isPlad(string):
        i=len(string)
        reverse=""
        while i>0:
            i-=1
            reverse+=string[i]            
        print(reverse)
        
        if string==reverse:
            return True
        return False

# O(1) Space, O(n) Time
def isPlad2(string):
    left=0
    right=len(string)-1

    # print(len(string)/2)
    for x in range(0,int(len(string)/2)):
        if string[left]==string[right]:
            pass
        elif string[left]!=string[right]:
            return False
        left+=1
        right-=1

    return True


if __name__ == "__main__":
    print(isPlad('racecar'))
    print(isPlad2('racecar'))
    