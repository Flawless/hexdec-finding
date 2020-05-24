#!/usr/bin/env python

import socket
import re

TCP_IP = '109.233.56.90'
TCP_PORT = 11543
BUFFER_SIZE = 1024


def find(ending):
    end = 0
    number = 0
    n = len(ending)
    for i in range(0, n):
        end += int(ending[-i-1]) * 10**i
        while not ((hex(number % 16**(i+1)))[2:] == str(end)
                   and (number % 10 ** (i+1) == end)):
            number += 80**i
    return number


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    p = re.compile(b'.?ends in (\d+):.?')

    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        number = p.findall(data)
        print("<-: ", data)
        if len(number) > 0:
            ending = number[0].decode("utf-8")
            number = find(ending)
            if find is not None:
                data = str(number).encode("utf-8") + b'\r\n'
                s.send(data)
                print("->: ", data)
