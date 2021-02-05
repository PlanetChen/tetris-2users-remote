## _*_ coding:  utf-8 _*_
from socket import *
import threading

#test 2021.02.05 23.08

class Server(threading.Thread):
    def __init__(self):  # 初始化和销毁对象函数.
        threading.Thread.__init__(self)
        self.ADDR = ('', 21567)
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind(self.ADDR)
        self.thStop = False

    def __del__(self):  # 销毁函数.
        self.sock.close()

    def transMsg(self):
        (data, curAddr) = self.sock.recvfrom(1024)
        print '< ' + data

    def run(self):
        while not self.thStop:
            self.transMsg()

    def stop(self):
        thStop = True


class Client(threading.Thread):
    def __init__(self, ip, name):
        threading.Thread.__init__(self)
        self.ADDR = (ip, 21567)
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.uname = name
        self.thStop = False

    def __del__(self):
        self.sock.close()

    def sendMsg(self, msg):
        self.sock.sendto(self.uname + ': ' + msg, self.ADDR)

    def run(self):
        while not self.thStop:
            msg = raw_input()
            if not msg.strip():
                print u'< 输入内容为空!'
                continue
            print '> ' + self.uname + ':' + msg
            self.sendMsg(msg)

    def stop(self):
        thStop = True


def main():
    ip = raw_input(unicode('< 请输入对方的IP地址:', 'utf-8').encode('gbk'))
    name = raw_input(unicode('< 请输入您的昵称:', 'utf-8').encode('gbk'))
    cli = Client(ip, name)
    ser = Server()
    cli.start()
    ser.start()


if __name__ == '__main__':
    main()