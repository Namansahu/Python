a="naman"
len2 =len(a)
print(len2)


#index
str="naman sahu"
print(str[3])


str3 ="hello"

print(str+str3)


#slicing
print(str[1:5])
print(str[: :-1])  # reverse
print(str[-3:-1]) # negative index



#string function
str ="i am studing in NIT"
print(str.endswith("an"))
print(str.capitalize())# capital 1st value 
print(str.replace("a","o"))# replace all 
print(str.find("o"))    #first index of 1 st occur
print(str.count("i"))



# 
# name =input("enter first name : ")
# print(len(name))
# nsskjjjkk
# occure of $ in string 
dol=" hi my $ occur $ here "
print(dol.count("$"))




# conditional

marks=74
if(marks>=90):
    grade="A"
elif(marks>=80 and marks <90):
    grade="B"
else:
    grade="C"

print(grade)

