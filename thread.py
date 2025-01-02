from threading import Thread 
from time import sleep
class Mytrd1(Thread):
    def run(self):
        for i in range(1,50):
            print("hi from thread1")

        # while True:
        #     msg = input('please give a msg')
        #     print('u entered :: %s' %msg)
class Mytrd2(Thread):
    def run(self):
        for i in range(1,50):
            print("hi from threa2")

    # def run(self):
    #     while True:
    #         # msg = input('please give a msg')
    #         sleep(1)
    #         print('other user said :: bla bla')
t1= Mytrd1()
t2 = Mytrd2()
t1.start()
t2.start()
print("main i sdoing some work ")
t2.join()
print("="*50)
print(" main finished ")
print("=",50)
