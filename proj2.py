#! /usr/bin/env python

def EulerProj2():
  total = 0
  max = 4000000
  flag = True
  fib1 = 0
  fib2 = 1
  while flag == True:
    fib2 = fib1 + fib2
    if fib2 % 2 == 0:
      total = total + fib2
    if fib2 > max:
      flag = False
  print(total)

      
