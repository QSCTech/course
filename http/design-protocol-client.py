# client.py
import socket
from protocol import Session

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('127.0.0.1', 9999))

session = Session(s)

# 接收欢迎消息:
print(session.recv().data)
while (True):

    # 输入消息
    data = input("Enter data: ")
    session.send(data)
    msg = session.recv()
    print('%s. Now is %d' % (msg.data, msg.recv_time))
    if data == "exit":
        break

session.close()
