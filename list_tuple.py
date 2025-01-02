marks=[45.4,44,22.5,22.9]
print(marks)
print(len(marks))
print(type(marks))
student=["karan",95,"dell"] # hetrogenous
print(student)


#list is mutable
#slicing

print(marks[1:3])
print(marks[1:])
print(marks[:-3])

#list mathods

list=[4,2,6,27,7,45]
list.append(3)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(4,33)
print(list)
list.remove(4)
list.pop(5)
print(list)

# Tuple
#almost same as list immutable sequence 
tup=(2,4,6,1,7)
print(tup)
jj=(4,) #for one value of tuple
print(jj)

#slicing 
print(tup[1:])
#method 

print(tup.index(4)) # find value of x in tuple
print(tup.count(2))



#question
# list=[]
# a=input("enter 1")
# b=input("enter 2")
# c=input("enter 3")

# list.append(a)
# list.append(b)
# list.append(c)
# list.append(input("enter 4"))
# print(list)

# palindrome of elment if list contains

list1=[1,2,1]
list2 =[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1 ==list1):
    print("palindrome")
else:
    print("NOT palindrome")
