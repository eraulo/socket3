import socket


def Main():
    HOST = '127.0.0.1'    # The remote host
    PORT = 50007              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = input("->>>")
        while message != 'q':
            s.sendall(message.encode("utf-8"))
            data = s.recv(1024)
            print('Received', repr(data))
            message = input('->>>')
        s.close()

if __name__ == "__main__":
    Main()
