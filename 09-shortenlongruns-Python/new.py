
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

def fun(n):
    s=''
    for i in range(n):
        if(i%2==0):
            s+=' 1 '
            print(s)
        else:
            s+='0 '
            s=s[0:len(s)-1]
            print(s[::-1])
       

fun(5)

            
