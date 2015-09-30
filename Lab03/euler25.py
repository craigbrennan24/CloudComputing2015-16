#! /usr/bin/env python

def DigitFibonacci():
	fib1 = 0
	fib2 = 1
	temp = 0

	found = False
	fibCounter = 1
	while( found == False ):
		fibStr = str(fib2)
		fibCheck = len(fibStr)
		if( fibCheck >= 1000 ):
			found = True
		else:
			temp = fib2
			fib2 = fib2 + fib1
			fib1 = temp
			fibCounter += 1

	print "First 1k Digit Fib num = %d" % fib2
	print "Fib index = %d" % fibCounter

DigitFibonacci()
