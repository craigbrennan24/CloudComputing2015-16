#! /usr/bin/env python3

#Program that tests if input string is a palindrome, returns TRUE or FALSE

def Palindrome( s ):
	string = str(s)#Convert argument to string
	string = string.upper()#Change all characters to uppercase
	stringReverse = string[::-1]#Reverse string
#	print "%s" % string
#	print "%s" % stringReverse
	if( string == stringReverse ):
		print "TRUE"
	else:
		print "FALSE"

