# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

def fun(a):
	if(a==0):
		return 1
	b=1
	for i in range(a,1,-1):
		b=b*i
	return b
	
def fun_pascaltrianglevalue(row, col):
	if(row<0 or col<0):
		return None
	elif(col>row):
		return 0
	val=fun(row-col)*fun(col)
	res=int(fun(row)/val)
	return res

# fun_pascaltrianglevalue(0,0)
	