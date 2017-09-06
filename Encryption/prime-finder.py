from time import time

start = time()                  # Start the timer

r = int (input( "Upto what number do you wish to find prime numbers?  "))
for n in range (1,r,1):
    c=0
    
    for i in range(1, n, 1):    # goes through all the numbers 1 to  n
        p=n%i                   # This gives the remainder
        if p == (0):            # If the remainder is zero it is a factor
            c=c+1               # This counts the factors
        
    if c <= (1):                # If there are only one factors it is a prime number
        print (str(n)+" is a prime number")


end = time()                    # Stop the timer
total = end - start
print(int (total))
print( str(total) + " seconds" )


'''
Factoring is like taking a number apart. It means to express a number as the product of its factors.
Factors are either composite numbers or prime numbers (except that 0 and 1 are neither prime nor composite).
The number 12 is a multiple of 3, because it can be divided evenly by 3.
'''
