#! /usr/bin/env python

def EulerProj2():
  loop = True
  total = 0
  max = 4000000
  fib1 = 0
  fib2 = 1
  fib3 = 0
  while loop == True:
    fib3 = fib2
    fib2 = fib2 + fib1
    fib1 = fib3
    if fib2 > max:
      loop = False
    elif fib2 % 2 == 0:
      total = total + fib2
  print( total )

EulerProj2()
    
