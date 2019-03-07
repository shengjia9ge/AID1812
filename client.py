from socket import *

#创套接字
sockfd = socket()

#发起连接
server_addr = ('172.40.71.149',8888)
sockfd.connect(server_addr)

#收发消息
#发
data = input(">>")
sockfd.send(data.encode())

#收
data = sockfd.recv(4096)
print("From server:",data.decode())

#关闭套接子
sockfd.close()
