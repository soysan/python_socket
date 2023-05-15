# -*- coding : UTF-8 -*-

import socket
import threading
import time

import yaml


with open('config.yml', 'r') as conf:
    c = yaml.safe_load(conf)


class Client(threading.Thread):

    def run(self):
        count = 5
        while count > 0:
            count -= 1
            time.sleep(1)

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((c['network']['host'], c['network']['port']))
            print('connect client')
            client.sendall('test'.encode('utf-8'))
            data = client.recv(1024)

        print('received', data)


if __name__ == '__main__':
    cli = Client()
    cli.start()
    cli.connect()
