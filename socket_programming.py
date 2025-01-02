# socket programming

from socket import socket,gethostname
s1 =socket()
port =12321

hn =gethostname()
s1.bind((hn,port))
print(1)

s1.listen(4) # max no client can wait 

while True:
    print(2)
    s2, addr=s1.accept()
    print(3)
    print("connected with ", addr)

    while True:
        msg= s2.recv(1024).decode();
        print('Client said %s ' %msg)
        msg2 = 'you said :: %s' % msg 
        if msg == "exit":
            break
        elif msg.find("vacation")>= 0:
            msg2 ="how was ur last vacation?"
        s2.send(msg2.encode())

