#! /usr/bin/env python3

#Program that tests if input string is a palindrome, returns TRUE or FALSE

def Palindrome( s ):
	string = str(s)
	string = string.upper()
	stringReverse = string[::-1]
	print "%s" % string
	print "%s" % stringReverse
	if( string == stringReverse ):
		print "TRUE"
	else:
		print "FALSE"

