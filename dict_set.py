info ={
    "name": "naman",
    "key" : "value",
    "learning": "coding",
    "age" :35,
 "is_adult": True,
 "subject": ["python","c","java"],
 "topic": ("dict","set")
}
print(info)
# unordered  , mutuable , dont allow duplicate key

print(info["age"])
info["name"] ="mansi"
print(info["name"])

null_dict={}
null_dict["name"] ="naman"
print(null_dict)


#nested dict value ->  dict 

student ={
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 100
    }
}
print(student["subjects"]["chem"])


'''
#method

print(student.keys()) # all key 
print(len(list(student.keys())))

print(list(student.values()))

print(student.items()) # list of all key : pairs
print(student.get("name")) # get data  without error

student.update({"city": "delhi"})
print(student)


# set in python , uniques and immutable 

set={1,3,5}
print(set)
# set not allow to stare list and dict
null_set =set()
print(null_set)

collection =set()

collection.add(1)
collection.add(2)
print(collection)
collection.remove(2)
collection.clear()


'''

marks={

}
n =3
# for i in n:
#     x = int(input("enter ",i))
# print(x)
