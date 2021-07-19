# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	n=abs(digit)
	c=-1
	while(n>0):
		val=n%10
		c=c+1
		n=n//10
		if(c==k):
			return val
	if(k>c):
		return 0
