# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def prime(n):
	if(n<=1):
		return False
	if(n==2):
		return True
	if(n%2==0):
		return False
	for j in range(3,n):
		if(n%j==0):
			return False
	return True


def happy(m):
	sum1=0
	while(m>0):
		n=m%10
		sum1+=(n**2)
		m=m//10
	return sum1


def fun_nth_happy_prime(n):
	i=1
	res=[]
	while(len(res)<=n):
		if(prime(i)):
			s=i
			for j in range(30):
				p=happy(s)
				# print(p,'p')
				if(p==1):
					res.append(i)
					break
				# if('4' in str(p)):
				# 	break
				s=p
		i=i+1
	print(res)
	return res[n]

# print(happy(100))
# print(fun_nth_happy_prime(3))

