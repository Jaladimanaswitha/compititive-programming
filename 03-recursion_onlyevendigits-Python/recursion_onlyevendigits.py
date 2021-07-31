# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.


def zro(a,b=''):
	print(a)
	if(a<10):
		if(a%2==0):
			b+=str(a)
			return b
		if(len(b)==0):
			return 0
	c=a%10
	if(c%2==0):
		b+=str(c)
	return zro((a//10),b)

def fun(l,p):
	if(len(l)==0):
		return p
	a=str(zro(l[0]))
	a=a[::-1]
	p.append(int(a))
	# print(p,'p')
	return fun(l[1:],p)

def fun_recursion_onlyevendigits(l):
		p=[]
		return fun(l,p)

print(fun_recursion_onlyevendigits([5, 0 , 66, 82, 121]))
