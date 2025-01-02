class student:
    college_name="ABC "
    def __init__(self,name,marks): # constructor
        print("create new student")
        self.name=name
        self.marks=marks # obj attr > class attr
    name="karan"

    def welcome(self):
        print("welcome student")

    def get_marks(self):
        return self.marks
s1 =student("naman",87)
print(s1.name)
s1.welcome()
# class oj=bject


s2= student("dhan",99)
print(s2.name)
print(s2.college_name)

# method  function belonmg  to obj
# attribute class and instance 

# common thing is used in class sttribute  whereas things which is different with object is as instance atrribite 



class stu:
    def __init__(self,name,marks):
        self.name=name
        self.marks =marks
    def get_avg(self):
        sum =0
        for val in self.marks:
            sum+= val
        print("hi",self.name,"your avg score is ",sum/3)
s1=stu("naman",[89,95,94])
s1.get_avg()


# static methods 
# dont use self  work at class level 

class stu:
    def __init__(self,name,marks):
        self.name=name
        self.marks =marks
    @staticmethod
    def hello():
        print("hello")
    
    def get_avg(self):
        sum =0
        for val in self.marks:
            sum+= val
        print("hi",self.name,"your avg score is ",sum/3)
s1=stu("naman",[89,95,94])
s1.get_avg()
s1.hello()




class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.cluch=False
    def start(self):
        self.cluch=True
        self.acc=True# abstraction 
        print("car started")
car1=car()
car1.start()



# account balance credit debit 


class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    def debit(self,amount):
        self.balance-= amount
        print("Rs ",amount,"was debited")
        print("total balance =",self.get_balance())
    def credit(self,amount):
        self.balance  += amount
        print("Rs ",amount,"was credited")
        print("total balance =",self.get_balance())
    def get_balance(self):
        return self.balance
    
acc1 =Account( 10000 ,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(89000)        
acc2 =Account( 10000 ,12345)
acc2.debit(1000)
acc2.credit(500)
acc2.credit(89000)   
# del acc2
# print(acc2)
# del obj



# access specificer 
# private __

class person:
    __name="anonymous"

    def __hello(self):
        print("hello ")
    def welcome(self):
        self.__hello()
p1 =person()
# print(p1.__name)
# print(p1.__hello)
print(p1.welcome())



# inheritance 

