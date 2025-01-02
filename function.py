# function in python 
# redundent code 
def calsum(a,b): # defination  
    sum =a+b
    print(sum)
    return sum


calsum(2,4) # caall


def printhello():
    print("HEllo")

printhello()
printhello()


# avg od 3 

def calavg(a,b,c):
    sum =a+b+c
    avg =sum/3
    print(avg)
    return avg
calavg(1,4,6)
# length of list 
cities=["delhi", "noida", "pune", "banglore"]

def print_len(list):
    print(len(list))

print_len(cities)

# print ele of list in single line


def print_list(list):
    for item in list :
        print(item, end=" ")
print_list(cities)

# factorial of number 

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)


factorial(5)


# convert USD to INr

def converter(usd):
    inr = usd*83
    print(usd,"USD = ", inr, "INR")

converter(7)

# odd =ODD even =EVEN

def even_odd(n):
    if (n%2 ==0):
        return "EVEN"
    else:
        return "ODD"
eo=even_odd(9)
print(eo)


# recursion  kaam , base case , call stack
print("-------------------------------------")
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
show(5)


# factorial n =n-1 *n

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n

print(fact(7))

# sum of first n 
def sum_n(n):
    if(n==0):
        return 0
   
    return sum_n(n-1)+ n
print(sum_n(7))


# all element in list  
# ind a 

def print_list(list,idx=0):
    if(idx ==len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)
car =["BMW", "JAGUAR","MEREDEC"]
print_list(car)