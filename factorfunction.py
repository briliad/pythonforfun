import math

def getprimes(x):
    y = (x // 2) + 1   #int(math.sqrt(x))
   
    primes = [2]
    num = 2
    while num < y:        
        for x in primes:
            d = False
            if (num % x == 0):
                d = True
                break
        if not d:
            primes.append(int(num))
        num = num + 1
    return primes


def getfactors(num, primes):
    z = int(num)
    
    factors = []

    while z > 1:
        for y in primes:
            #print (int(num) % int(y))
            a = num % y
            print (y, a)
            if num >= y and a == 0:
                factors.append(y)
                z = z // y
                print (z, y)
                exit
    return factors

print (getprimes(10))

h = getprimes(10)
print (getfactors(10, h))
#print (5 % 2)