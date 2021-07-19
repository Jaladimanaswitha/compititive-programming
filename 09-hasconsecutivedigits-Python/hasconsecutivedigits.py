# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n=abs(n)
	m=str(n)
	for i in range(len(m)-1):
		if(m[i]==m[i+1]):
			return True
	return False
