import math




def compute(f):
    n = 1

    while True:
        val = f(n,2) * (10 ** -6)
        if (val >= 1):
            print n
            break
        n += 1

      

   
    

#print 1000 * 10 ** -6


compute(math.pow) 
#compute(math.sqrt)    











