# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

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


def factors(n):
    m=n
    p=[]
    i=2
    while(i<=n):
        if(n%i==0):
            n=n//i
            if(prime(i)):
                if(m!=i):
                    p.append(i)
            continue
        i+=1
    return p

def sum_as(m):
    s=0
    for i in m:
        s+=dig_sum(i)
    return s

def dig_sum(n):
    c=0
    while(n>0):
        c+=n%10
        n=n//10
    return c


def fun_nth_smithnumber(n):
    i=1
    res=[]
    while(len(res)<=n):
        p=factors(i)
        a=sum_as(p)
        c=dig_sum(i)
        if(a==c):
            # print(p,a,c)
            res.append(i)
        i+=1
    return res[n]


print(fun_nth_smithnumber(19))