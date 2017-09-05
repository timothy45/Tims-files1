
n = int (input( "What number"))
c=0
for i in range(1, n, 1):
    p=n%i
    
    if p == (0):
        print ("These are the factors of " +str (n)+" are "+ str(i))
        c=c+1
        
if c <= (1):
    print (str(n)+" is a prime number")
