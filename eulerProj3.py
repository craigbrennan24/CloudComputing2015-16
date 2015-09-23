#! /usr/bin/env python
import math

def EulerProj3():
  largest = 0
  i = 1
  target = 600851475143
  lastPercent = 0
  currentPercent = 0
  while True:
    if target % i == 0:
      test = isPrime(i)
      if test == True:
        largest = i
        print "%d POTENTIAL MATCH" % largest
    if i == math.ceil(math.sqrt(target)):
      break
    if i % 1000000000 == 0:
      print(i)
    if currentPercent != lastPercent:
      print currentPercent
      lastPercent = currentPercent
    currentPercent = math.ceil(percentage(i, target))
    i = i + 2
  print "%d MATCH" % largest
      
def percentage(part, whole):
  return 100 * float(part)/float(whole)

def isPrime(x):
  result = True
  for i in range(3, int(math.ceil(math.sqrt(x)))):
    primeTest = isPrime(i)      
    if primeTest == True:
      if x % i == 0:
        result = False
        break
  return result

EulerProj3()
