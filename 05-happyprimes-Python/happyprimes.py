# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

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

def sumOfSquaresOfDigits(num):
    s=0
    while(num>0):
        a=num%10
        num=num//10
        s+=pow(a,2)
    return s



def ishappyprimenumber(n):

    m=sumOfSquaresOfDigits(n)
    while(m!=n and m!=4):
        # print(m,'m')
        if(m==1):
            return True
        m=sumOfSquaresOfDigits(m)
    return False

    # Your code goes here
    
print(ishappyprimenumber(940))
print(ishappyprimenumber(820))
print(ishappyprimenumber(1418854))
print(ishappyprimenumber(709))