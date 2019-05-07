'''
This function is the chr() in python but renamed for readability

	chr() method returns a character (a string) from an 
	integer (represents unicode code point of the character).

	Parameters:
	The chr() method takes a single parameter, an integer i.
	The valid range of the integer is from 0 through 1,114,111.

	Returns:
	a character (a string) whose Unicode code point is the integer i
'''

def to_unicode(integer):
	return chr(integer)
