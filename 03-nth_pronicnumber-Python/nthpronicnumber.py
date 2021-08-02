# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	# Your code goes here
	res=[]
	i=0
	while(len(res)<=n):
		for j in range(-1,i+1):
			if(j*(j+1)==i):
				res.append(i)
				break
		i+=1
	return res[n]
	print(res[n])


# nthpronicnumber(13)