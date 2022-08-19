import socket
from time import sleep

def simple_client(host, port, message):
    with socket.socket() as sock:
        close = False
        try:
            sock.settimeout(3)
            sock.connect((host, port))
            sock.sendall(bytes(message, 'utf-8'))
            data = sock.recv(1024).decode("utf-8")
            print(f'From server answear:  {data}')
            if data == 'Bye':
                close = True
                return close
        except ConnectionRefusedError:
            sleep(0.5)




if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8000

    while True:
        print('Please, type simple math operation(3+3):')
        MESSAGE = input()
        if simple_client(HOST, PORT, MESSAGE):
            break

