def one_to_n(n):
    for i in range(n):
        print(i)

def product_even(n):
    p=1
    for i in range(1,n+1):
        if i%2==0:
            p=p*i
        
    print(p)

def rev_num(n):
    rev=0
    while n>0:
        digit=n%10
        rev= rev*10+digit
        n=n//10
    print(rev)

def is_prime(k):
    if k<=1:
        return 0
    
    for i in range(2,k):
        if k%i==0:
            return 0
        
    return 1
    


def sum_of_prime(n):
    sum=0
    for i in range(2,n):
        if is_prime(i) == 1:
            sum=sum+i
        
    print(sum)

    

number=int(input("Enter Your Choice:"))
match number:
    case 1: 
        n= int(input("enter number to print"))
        one_to_n(n)
    case 2:
        n= int(input("enter number:"))
        product_even(n)
    case 3:
        n= int(input("enter number:"))
        rev_num(n)
    case 4:
        n= int(input("enter number:"))
        sum_of_prime(n)






