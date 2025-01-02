# loop used to repeat 
# c=1
# while c<5:
#     print("hello")
#     c+=1



i=1;
while i<=5:
    print(i)
    i+=1

 # num 1 to 100
 # 

i=1
while i<=100:
    print(i)
    i+=1  

# 100 to 1
i=100
while i>=1:
    print(i)
    i-=1 
# multip  of n  3 =3 *1
 
# i =1
# n=3
# while i<=10:
#     print(n*i)
#     i+=1
# sqrott

# travese  
num=[1,4,9,16,25,36,49,64,81,100]

i=0
while(i< len(num)):
    print(num[i])
    i+=1

# search for number x in this tuple using loop 
num=(1,4,9,16,25,36,49,64,81,100)
x =36
i =0
while i< len(num):
    if(num[i]==x):
        print("found")
        breakpoint
    else:
        print("not found")
        # continue
    i+=1

# break


# for loop sequence travese 

num=[1,2,3,4,5]
for vl in num:
    print(vl)

tupo=(1,2,4,5,)
for val in tupo:
    print(val)
else : # optiomnal else 

    print(2)


num=[1,4,9,16,25,36,49,64,81,100]
num1=(1,4,9,16,25,36,49,64,81,100)

for val in num: # list
    print(val)
for val in num1:# tuple
    if (val == x):
        print("found")
    print(val)

# range  return sequense of number start with 0 steps size 1

seq= range(5)

for i  in range(1,5,2): # start stop step
    print(i) 


for i in range(2, 100 ,2):
    print(i) # even

# sum 
n =5
sum =0
for i in range(1,n+1):
    sum+=i
print(sum)

# factorial
fact =1
for i in range(1,n+1):
    fact*=i
print(fact)
