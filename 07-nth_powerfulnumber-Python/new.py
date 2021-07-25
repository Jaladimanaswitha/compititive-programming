# [
#     [1 1 1 1]
#     [1 2 3 4]
#     [1 3 6 10]
#     [1 4 10 20]

# ]

def fun(n):
    res=[0]*n
    m=[]
    for i in range(n):
        m.append(res)
    res=m
    print(res)
    for i in range(n):
        print(res)
        for j in range(n):
            if(i==0 or j==0):
                res[i][j]=1
            else:
                res[i][j]=res[i][j-1]+res[i-1][j]
    print(res)

fun(4)
