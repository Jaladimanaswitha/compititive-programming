# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

import math
def isperfectsquare(n):
	# your code goes here
	if(type(n)==str):
		if(n.isnumeric()==False):
			return False
	k=int(n)
	if(k<0):
		return False
	m=math.sqrt(k)
	print(int(m**2))
	if(int(m**2) == k):
		return True
	else:
		return False

print(isperfectsquare(625))