# tcp-server.py
import socket
import threading

# 创建 socket 实例
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定 ip 和端口（“127.0.0.1” 为回环地址，即本机）
s.bind(('127.0.0.1', 9999))

# 开始监听，允许挂起的最大连接数为 5
s.listen(5)
print('Waiting for connection...')


# 定义处理新连接的函数
def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)

    # 发送欢迎消息
    sock.send(b'Welcome!')

    # 循环接收消息
    while True:
        # 接收消息最大长度为 1024，返回类型为 bytes
        data = sock.recv(1024)

        # 如果收到 0 字节（收到 EOF，连接关闭）或‘ exit ’，退出循环
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


# 循环接受连接请求
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()
