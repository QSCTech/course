import time
import socket


class Message(object):
    def __init__(self, data: str):
        self.data = data
        self.recv_time = time.time()


class Session(object):
    def __init__(self, conn: socket.socket):
        self.conn = conn

    def _send(self, msg: Message):
        pass

    def send(self, msg: str):
        msg = Message(msg)
        self._send(msg)

    def recv(self) -> Message:
        pass

    def close(self):
        self.conn.close()
