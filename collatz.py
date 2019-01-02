def collatz(somenumber):
  
    if somenumber % 2 == 0:
      somenumber=somenumber//2
    else:
      somenumber=3*somenumber+1
    print(somenumber)
    return somenumber


print ('Enter a number')
someinput = int(input())

while collatz(someinput) != 1:
    someinput = collatz(someinput)