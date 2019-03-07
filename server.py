import socket

#创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0',8888))

#设置监听
sockfd.listen(5)
#等待处理客户连接
print("waitting for connect...")
connfd,addr = sockfd.accept()
print("Connect from",addr)#客户地址

#收发消息
#收
data = connfd.recv(1024)
print("Receive message",data.decode())
#发
n= connfd.send(b"Receve your message!!")
print("Send %d bytes"%n)
#关闭套接字
connfd.close()#连接套接字
sockfd.close()#监听套接字
