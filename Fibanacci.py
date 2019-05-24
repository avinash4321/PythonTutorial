def fib(n):
    a,b = 0,1
    if (n <= 0):
        print ('Enter value greater than 0')
    elif (n == 1):
        print (a)
    elif (n >= 2):
        print (a)
        print (b)
        for i in range(1,n-1):
            a,b = b, a+b
            print (b)


fib(10)