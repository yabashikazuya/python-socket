import threading
import socket
import time


class TestThread(threading.Thread):
    def __init__(self):
        super(TestThread, self).__init__()
        self.host = "localhost"
        self.port = 8765
        bufsize = 1024
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_msg = 0

    def run(self):
        print('send message')
        while True:
            try:
                self.sock.connect((self.host, self.port))
                break
            except ConnectionRefusedError:
                time.sleep(1)
        while True:
            print('sub')
            send_msg= str(self.send_msg).encode('utf-8')
            self.sock.send(send_msg)
            time.sleep(1)
            self.send_msg += 1

if __name__ == '__main__':
    th = TestThread()
    th.daemon = True
    th.start()

    for i in range(100000):
        print(i)
        time.sleep(1)
