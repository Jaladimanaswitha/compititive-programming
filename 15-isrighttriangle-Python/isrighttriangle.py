# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.



import math
def dis(x1,x2,y1,y2):
	dist=int((pow(x2-x1,2)+pow(y2-y1,2)))
	return dist

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# a=(int(pow((x1-x2),2))+int(pow((y1-y2),2)))
	# b=(int(pow((x2-x3),2))+int(pow((y2-y3),2)))
	# c=(int(pow((x3-x1),2))+int(pow((y3-y1),2)))
	# if ((a>0 and b>0 and c>0) and (a==(b+c) or b==(a+c) or c==(a+b))):
	# 	return True
	# else:
	# 	return False

	# your code goes here
	a=dis(x1,x2,y1,y2)
	b=dis(x3,x2,y3,y2)
	c=dis(x1,x3,y1,y3)
	p=a**2
	q=b**2
	r=c**2

	if(a<=0 or b<=0 or c<= 0.0):
		return False
	if(a+b<=c or b+c<=a or c+a<= b):
		return False
	elif(p+q==r or q+r==p or r+p==q):
		return True
	else:
		return False

print(isrighttriangle(13, -1, -9, 3, -3, -9))