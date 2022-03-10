def sum_of_series(N):
    sum=0
    for i in range(1,N+1):
        sum=sum+i
    return sum

def square(N):
    return N*N

def myFunction(*args):
    result=''
    for arg in args:
        result=result+arg+" "
    return result
    
s=lambda n:n*n*n

def validPassword(word):
    for char in word:
        if (char.isdigit()):
            contains_digit=True
    if(contains_digit):
         return("Valid Password")
    else:
        return("Invalid Password")
    
