import socket
import os

ip_addr = '127.0.0.1'
port = 9000
chunk_size = 512

file_name = input("Input your file name : ")
file_size = str(os.path.getsize(file_name))
# http://mwultong.blogspot.com/2007/04/python-file-size-in-bytes.html
# 위의 블로그를 참고하여서 파일 크기를 구하였다.

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.sendto(file_name.encode(), (ip_addr, int(port)))
socket.sendto(file_size.encode(), (ip_addr, int(port)))

transferred_size = 0
#print(type(transferred_size))
with open(file_name, 'r') as f:
    try:
        print("File Transmit Start....")
        while True:
            data = f.read(chunk_size)
            transferred_size = transferred_size + chunk_size
            if not data:
                transferred_size = int(file_size)
            socket.sendto(data.encode(), (ip_addr, int(port)))
            rate =  transferred_size / float(file_size) * 100
            print("Current_size / total_size = ", transferred_size, "/", file_size, ", ", rate, "%")
            if not data:
                #print(data)
                break
    except Exception as e:
        print(e)

print("ok")
print("file_send_end")
#data, addr = socket.recvfrom(2000)
#print(data)

#socket.sendto("Hello server".encode(), addr)