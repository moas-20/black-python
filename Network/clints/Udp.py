import socket

target_host = "www.google.com"
target_port = 80

# clien upd
client = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAABBBCCC" , (target_host , target_port))

# resv
data , addr = client.recvfrom(4096)

print(data.decode())

client.close()