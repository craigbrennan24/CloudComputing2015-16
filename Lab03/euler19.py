#! /usr/bin/env python

#How many sundays fell on the first month during the twentieth century (1 Jan 1901 - 31 Dec 2000)

def sundayCounter():
	startYear = 1900
	startDay = 1
	startMonth = 1
	targetYear = 2000
	
	for year in range(startYear, (targetYear+1)):
		for month in range( startMonth, 13 ):
			for day in range( 

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
	

def getDaysInMonth(x, y):
	#Returns the amt of days in specified month
	#x = month
	#y = year (to check if year is leap year)
	if( x == 4 or x == 6 or x == 9 or x == 11 ):
		#30 days has September, April, June and November
		return 30
	elif( x < 4 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12 ):
		#All the rest have 31... 
		return 31
	elif( x == 2 ):
		#Except for February, once in four: February has 1 day more
		if( isLeapYear(y) == True ):
			return 29
		else:
			return 28
