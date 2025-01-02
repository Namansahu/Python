# f =open("demo.txt","r")
# data=f.read()
# line1=f.readlines()
# print(line1)
# print(data)
# print(type(data))
# f.close()

f =open("sample.txt","w")
f.write("my name is autobot")
f.close()

f =open("sample.txt","a+")
f.write("I am optimus prime here to  save the world ")
f.close()


with open("demo.txt","r") as f:
    data=f.read()
    print(data)


# delete usinf module predefine 
# imprort od .remove

import os
os.remove("sample.txt")


with open("prac.txt","w") as f:
    f.write("my java is my java")
word="JAVA"
with open("prac.txt","r") as f:
    data = f.read()
    if(data.find(word)!=1):
        print("found")
    else:
        print("not found")
new_data = data.replace("JAVA","python")
print(new_data)



with open("prac.txt","w") as f:
    f.write(new_data)


def check_for_line():
    word="JAVA"
    data =True
    line_no =1
    with open("prac.txt","r") as f:
        while data:
            data =f.readline()
            if (word in data ):
                print(line_no)
                return
            line_no +=1

    return -1
print(check_for_line())