#! /usr/bin/env python

#How many sundays fell on the first month during the twentieth century (1 Jan 1901 - 31 Dec 2000)

def sundayCounter():
	startYear = 1900
	startDay = 1
	startMonth = 1
	targetYear = 2000
	
	for i in range(startYear, (targetYear+1)):


def isLeapYear(x):
	result = True
	if( x % 4 == 0 ): # if yr is divisible by 4
		#probably a leap year
		if( x % 100 == 0 ): # if yr is a century
			#century is only a leap year if divisible by 400
			if( x % 400 == 0 ):
				#century is leap year
			else:
				result = False
		else:
			result = False
	else:
		#if not divisible by 4 then definitely not a leap yr
		result = False
	
