#! /usr/bin/env python

def EulerProj4():
  start = 100
  max = 1000
  largest = 0
  for i in range( start, max ):
    for j in range( start, max ):
      test = i * j
      stringTest = str(test)
      reverseTest = stringTest[::-1]
      if ( stringTest == reverseTest and
           largest < test):
        largest = test
        print "Found %d" % largest
  print "Answer = %d" % largest

EulerProj4()
