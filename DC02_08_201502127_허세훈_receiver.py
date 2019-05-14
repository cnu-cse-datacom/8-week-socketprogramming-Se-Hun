import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 9000))
chunk_size = 512

file_name, addr = server_socket.recvfrom(2000)
print("file recv start from ", addr[0])
print("File Name : ", file_name.decode())

file_size, addr = server_socket.recvfrom(2000)
print("File Size : ", file_size.decode())

transferred_size = 0
with open('./data/' + file_name.decode(), 'w') as f:
    try:
        print("File Transmit Start....")
        while True:
            transferred_size = transferred_size + chunk_size
            data, addr = server_socket.recvfrom(chunk_size * chunk_size)
            if not data:
                transferred_size = int(file_size)
            f.write(data.decode())
            rate =  transferred_size / float(file_size) * 100
            print("Current_size / total_size = ", transferred_size, "/", str(file_size.decode()), ", ", rate, "%")
            if not data:
                break
    except Exception as e:
        print(e)
        #if 


#file_name = server_socket.recvfrom(2000)

#file_name = server_socket.recvfrom(2000)
#print(file_name)

#server_socket.sendto("Hello client".encode(), addr)