# client socket 

# socket programming

from socket import socket,gethostname
c1 =socket()
port =12321

hn =gethostname()
c1.connect((hn,port))

while True:
    msg = input("Please enter a msg ")
    c1.send(msg.encode())
    if msg =="exit":
        break
    msg2= c1.recv(1024).decode();
    print('server said %s ' %msg2)
    