# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	flag=True
	if(n<0):
		n=-(n)
		flag=False
	a=[]
	b=k
	while(k>=0):
		if(k!=0):
			a.append(n%10)
		n=n//10
		k=k-1
	# print(n)
	n=(n*10)+d
	for i in range(len(a)-1,-1,-1):
		n=(n*10)+a[i]
		# print(n)
		# b=b-1
	# print(n)
	if(flag):
		return (int(n))
	else:
		return -(int(n))

fun_set_kth_digit(468,2,1)
	
	



