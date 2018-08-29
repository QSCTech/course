# tcp-client.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('127.0.0.1', 9999))

# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
while (True):

    # 输入消息
    data = input("Enter data: ")
    s.send(data.encode("utf-8"))
    print(s.recv(1024).decode('utf-8'))
    if data == "exit":
        break

s.close()
