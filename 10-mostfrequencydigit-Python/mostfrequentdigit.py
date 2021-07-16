# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	m=str(n)
	res=0
	val=0
	for i in m:
		if(m.count(i)>res):
			res=m.count(i)
			val=int(i)
		elif(m.count(i)==res):
			if(val>int(i)):
				val=int(i)
	return val
	
