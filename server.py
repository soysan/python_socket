# -*- coding : UTF-8 -*-

import socket
import threading
import yaml
import time

with open('config.yml', 'r') as conf:
    c = yaml.safe_load(conf)


class Server(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__connect: socket.socket or None = None

    def run(self):
        count = 5
        while count > 0:
            count -= 1
            time.sleep(1)
    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((c['network']['host'], c['network']['port']))
            server.listen(1)
            conn, addr = server.accept()
            print(f'started server with {addr}')
            self.__connect = conn

    def receive(self):
        with self.__connect:
            while True:
                data = self.__connect.recv(1024)
                if not data:
                    break
                self.__connect.sendall(data)


if __name__ == '__main__':
    ser = Server()
    ser.start()
    ser.connect()
    ser.receive()
