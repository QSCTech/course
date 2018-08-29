# http-client.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect((input('HOST:'), int(input('PORT:'))))

# 按照 HTTP 协议发送标准请求包
s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
print(s.recv(1024))
s.close()
