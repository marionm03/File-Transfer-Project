import socket, server                  # Import socket module
from Crypto.Cipher import AES

s = socket.socket()             # Create a socket object
host = "192.168.66.1"           #Ip address that the TCPServer  is there
port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
msg_c= "Hello server!"
s.send(msg_c.encode())

with open('received_file', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        #print('data=%s', (data))
        print(data.decode())
        if not data:
            break
        # write data to a file
        f.write(data)

key = b'abcd1234efgh5678'
cipher = AES.new(key, AES.MODE_EAX, nonce=server.nonce)
plaintext = cipher.decrypt(server.ciphertext)
try:
    cipher.verify(server.tag)
    print("The message is authentic:", plaintext)
except ValueError:
    print("Key incorrect or message corrupted")

f.close()
print('Successfully get the file')
s.close()
print('connection closed')


