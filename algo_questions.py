# Recursive Fibonacci function
 def Fibonacci(n):
    if n<=0:
        print("DNE")
    #  number is 0
    elif n==1:
        return 0
    # number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)