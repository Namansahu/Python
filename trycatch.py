# exception handiling 
class ECExceptio(Exception):
    pass
def getAccBal(rn):
    if rn > 0:
        print('acc bal for %d ' % rn)
    else:
        raise ECExceptio(" incorrect rn %d" % rn)
getAccBal(2)
try:
    print("db open")
    print(1)
    f1=open("c:\\nahihai.txt", "r")
    i=1/0
    print(2)
except IOError as e:
    print("3 sp")
except Exception as e:
    print("3 gen")
    print(e)
finally:
    print("db close")
print(4)




